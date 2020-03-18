from django.core.management.base import BaseCommand
from gaspoints.models import Point, CommercialType, PointType, Sinonim
from my_user_app.models import MyUser

import requests
class Command(BaseCommand):

    def handle(self, *args, **options):
        domain='https://transparency.entsog.eu/api/v1/connectionpoints'
        url=f'{domain}?limit=2000'
        result=requests.get(url).json()

        pointType=set([i['pointType'] for i in result['connectionpoints']])
        # PointType.objects.all().delete()
        for i in pointType:
            try:
                PointType.objects.create(name=str(i))
            except:
                pass

        commercialType=set([i['commercialType'] for i in result['connectionpoints']])
        # CommercialType.objects.all().delete()
        for i in commercialType:
            try:
                CommercialType.objects.create(name=str(i))
            except:
                pass


        # Point.objects.all().delete()
        for i in result['connectionpoints']:
            try:
                Point.objects.create(pointKey=i['pointKey'], pointLabel=i['pointLabel'], point_id=i['id'],
                                 commercialType=CommercialType.objects.filter(name=i['commercialType']).first(),
                                 pointType=PointType.objects.filter(name=i['pointType']).first(),
                                     user=MyUser.objects.filter(username='Lenin').first())
            except:
                pass

        # сразу к ней добавим первый синоним
        for i in result['connectionpoints']:
            try:
                Sinonim.objects.create(name=i['pointLabel'],
                                       root_point= Point.objects.filter(pointLabel=i['pointLabel']).first(),
                                       user=MyUser.objects.filter(username='Lenin').first())
            except:
                pass




