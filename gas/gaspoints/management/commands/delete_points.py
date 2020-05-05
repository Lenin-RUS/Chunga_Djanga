from django.core.management.base import BaseCommand
from gaspoints.models import Point, CommercialType, PointType, Sinonim, ExportCountry



class Command(BaseCommand):

    def handle(self, *args, **options):
        PointType.objects.all().delete()
        CommercialType.objects.all().delete()
        Point.objects.all().delete()
        Sinonim.objects.all().delete()
        ExportCountry.objects.all().delete()
