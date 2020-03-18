from django.db import models
from django.contrib.auth.models import AbstractUser


class Place_of_job(models.Model):
    name=models.CharField(max_length=32, unique=True)
    def __str__(self):
        return self.name

class MyUser(AbstractUser):
    email=models.EmailField(unique=True)
    job=models.ForeignKey(Place_of_job, on_delete=models.CASCADE)




# Create your models here.
