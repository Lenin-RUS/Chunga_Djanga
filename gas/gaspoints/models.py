from django.db import models
from my_user_app.models import MyUser
import requests


# Create your models here.
class AddNameTotable(models.Model):
    name=models.CharField(max_length=32, unique=True)
    class Meta:
        abstract=True

class TimeStapm(models.Model):
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class CommercialType(AddNameTotable):
    def __str__(self):
        return self.name

class PointType(AddNameTotable):
    def __str__(self):
        return self.name

class Point(TimeStapm):
    pointKey=models.CharField(max_length=32, unique=True)
    pointLabel=models.TextField(blank=False)         # <----------------- по идее тоже можно в нейм переименовать
    commercialType=models.ForeignKey(CommercialType, on_delete=models.CASCADE)
    pointType=models.ForeignKey(PointType, on_delete=models.CASCADE)
    point_id=models.CharField(max_length=32, unique=True)
    user=models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not Sinonim.objects.filter(root_point=self).exists():
            Sinonim.objects.create(root_point=self, name=self.pointLabel,  user=self.user)

    def __str__(self):
        return self.pointLabel

class Sinonim(AddNameTotable, TimeStapm):
    root_point=models.ForeignKey(Point, on_delete=models.CASCADE)
    user=models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

def pars():
    new_points=[]
    domain='https://transparency.entsog.eu/api/v1/connectionpoints'
    url=f'{domain}?limit=2000'
    result=requests.get(url).json()
    pointType=set([i['pointType'] for i in result['connectionpoints']])
    for i in pointType:
        try:
            PointType.objects.create(name=str(i))
        except:
            pass

    commercialType=set([i['commercialType'] for i in result['connectionpoints']])
    for i in commercialType:
        try:
            CommercialType.objects.create(name=str(i))
        except:
            pass
    for i in result['connectionpoints']:
        try:
            Point.objects.create(pointKey=i['pointKey'], pointLabel=i['pointLabel'], point_id=i['id'],
                                 commercialType=CommercialType.objects.get(name=i['commercialType']),
                                 pointType=PointType.objects.get(name=i['pointType']),
                                 user=MyUser.objects.get(username='Lenin'))
            new_points.append(i['pointLabel'])
        except:
            pass
      # сразу к ней добавим первый синоним
    for i in result['connectionpoints']:
        try:
            Sinonim.objects.create(name=i['pointLabel'],
                                   root_point= Point.objects.get(pointLabel=i['pointLabel']),
                                   user=MyUser.objects.get(username='Lenin'))
        except:
            pass
    print(new_points)
    return new_points
