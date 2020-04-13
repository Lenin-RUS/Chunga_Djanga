from django.core.management.base import BaseCommand
from gaspoints.models import Point, CommercialType, PointType, Sinonim, ExportCountry
from my_user_app.models import MyUser
import requests

class Command(BaseCommand):

    def handle(self, *args, **options):
        PointType.objects.all().delete()
        CommercialType.objects.all().delete()
        Point.objects.all().delete()
        Sinonim.objects.all().delete()
        ExportCountry.objects.all().delete()
