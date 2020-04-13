from django.core.management.base import BaseCommand
from gaspoints.models import Point, CommercialType, PointType, Sinonim, ExportCountry
from my_user_app.models import MyUser
import requests

class Command(BaseCommand):

    def handle(self, *args, **options):
        domain='https://transparency.entsog.eu/api/v1/connectionpoints'
        url=f'{domain}?limit=2000'
        result=requests.get(url).json()

        PointType.objects.all().delete()
        CommercialType.objects.all().delete()
        Point.objects.all().delete()
        Sinonim.objects.all().delete()
        ExportCountry.objects.all().delete()

        pointType=set([i['pointType'] for i in result['connectionpoints']])
        print(pointType)
        for i in pointType:
            try:
                PointType.objects.create(name=str(i))
            except:
                pass

        commercialType=set([i['commercialType'] for i in result['connectionpoints']])
        print(commercialType)
        for i in commercialType:
            try:
                CommercialType.objects.create(name=str(i))
            except:
                pass


        importFromCountryLabel=set([i['importFromCountryLabel'] for i in result['connectionpoints']])
        print(importFromCountryLabel)
        for i in importFromCountryLabel:
            try:
                ExportCountry.objects.create(name=str(i))
            except:
                pass


        for i in result['connectionpoints']:
            try:
                if i['importFromCountryLabel']:
                    Point.objects.create(pointKey=i['pointKey'], pointLabel=i['pointLabel'], point_id=i['id'],
                                        point_map_x=i['tpMapX'], point_map_y=i['tpMapY'],
                                        point_export_from=ExportCountry.objects.get(name=i['importFromCountryLabel']),
                                        commercialType=CommercialType.objects.get(name=i['commercialType']),
                                        pointType=PointType.objects.get(name=i['pointType']),
                                        user=MyUser.objects.get(username='Lenin'))
                else:
                    Point.objects.create(pointKey=i['pointKey'], pointLabel=i['pointLabel'], point_id=i['id'],
                                         point_map_x=i['tpMapX'], point_map_y=i['tpMapY'],
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