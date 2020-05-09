from django.conf.urls import url, include
from .models import Point, ExportCountry, CommercialType, PointType, Sinonim
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class PointSerializer(serializers.HyperlinkedModelSerializer):
    pointType=serializers.StringRelatedField()
    commercialType=serializers.StringRelatedField()
    class Meta:
        model = Point
        exclude = ['user']

class ExportCountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExportCountry
        fields = '__all__'

class CommercialTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommercialType
        fields = '__all__'

class PointTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PointType
        fields = '__all__'

class SinonimSerializer(serializers.HyperlinkedModelSerializer):
    # root_point=serializers.StringRelatedField()
    class Meta:
        model = Sinonim
        exclude = ['user']