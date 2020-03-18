from django.db import models
from my_user_app.models import MyUser


class AddNameTotable(models.Model):
    name=models.CharField(max_length=32, unique=True)
    class Meta:
        abstract=True


# Create your models here.
class CommercialType(AddNameTotable):
    def __str__(self):
        return self.name

class PointType(AddNameTotable):
    def __str__(self):
        return self.name

class Point(models.Model):
    pointKey=models.CharField(max_length=32, unique=True)
    pointLabel=models.TextField(blank=False)         # <----------------- по идее тоже можно в нейм переименовать
    commercialType=models.ForeignKey(CommercialType, on_delete=models.CASCADE)
    pointType=models.ForeignKey(PointType, on_delete=models.CASCADE)
    point_id=models.CharField(max_length=32, unique=True)
    user=models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.pointLabel

class Sinonim(AddNameTotable):
    root_point=models.ForeignKey(Point, on_delete=models.CASCADE)
    user=models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
