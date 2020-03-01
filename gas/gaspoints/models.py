from django.db import models

# Create your models here.
class CommercialType(models.Model):
    name=models.CharField(max_length=32, unique=True)
    def __str__(self):
        return self.name

class PointType(models.Model):
    name=models.CharField(max_length=32, unique=True)
    def __str__(self):
        return self.name

class Point(models.Model):
    pointKey=models.CharField(max_length=32, unique=True)
    pointLabel=models.TextField(blank=False)         # <----------------- по идее тоже можно в нейм переименовать
    commercialType=models.ForeignKey(CommercialType, on_delete=models.CASCADE)
    pointType=models.ForeignKey(PointType, on_delete=models.CASCADE)
    point_id=models.CharField(max_length=32, unique=True)
    def __str__(self):
        return self.pointLabel

class Sinonim(models.Model):
    name=models.CharField(max_length=32, unique=True)
    root_point=models.ForeignKey(Point, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
