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




