from django.core.management.base import BaseCommand
from gaspoints.models import Point, CommercialType, PointType

import requests
class Command(BaseCommand):

    def handle(self, *args, **options):
        domain='https://transparency.entsog.eu/api/v1/connectionpoints'
        url=f'{domain}?limit=2000'
        result=requests.get(url).json()

        pointType=set([i['pointType'] for i in result['connectionpoints']])
        PointType.objects.all().delete()
        for i in pointType:
            PointType.objects.create(name=str(i))

        commercialType=set([i['commercialType'] for i in result['connectionpoints']])
        CommercialType.objects.all().delete()
        for i in commercialType:
            CommercialType.objects.create(name=str(i))

        Point.objects.all().delete()
        for i in result['connectionpoints']:
            Point.objects.create(pointKey=i['pointKey'], pointLabel=i['pointLabel'], point_id=i['id'],
                                 commercialType=CommercialType.objects.filter(name=i['commercialType']).first(),
                                 pointType=PointType.objects.filter(name=i['pointType']).first())

