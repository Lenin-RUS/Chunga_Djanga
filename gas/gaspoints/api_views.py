from django.conf.urls import url, include
from .models import Point, ExportCountry, CommercialType, PointType, Sinonim
from rest_framework import routers, serializers, viewsets
from .serializers import PointSerializer, ExportCountrySerializer, CommercialTypeSerializer, PointTypeSerializer, SinonimSerializer

# ViewSets define the view behavior.
class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

class ExportCountriesViewSet(viewsets.ModelViewSet):
    queryset = ExportCountry.objects.all()
    serializer_class = ExportCountrySerializer

class CommercialTypeViewSet(viewsets.ModelViewSet):
    queryset = CommercialType.objects.all()
    serializer_class = CommercialTypeSerializer

class PointTypeViewSet(viewsets.ModelViewSet):
    queryset = PointType.objects.all()
    serializer_class = PointTypeSerializer

class SinonimViewSet(viewsets.ModelViewSet):
    queryset = Sinonim.objects.all()
    serializer_class = SinonimSerializer