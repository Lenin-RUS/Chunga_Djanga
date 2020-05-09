from django.conf.urls import url, include
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from .models import Point, ExportCountry, CommercialType, PointType, Sinonim
from rest_framework import routers, serializers, viewsets
from .serializers import PointSerializer, ExportCountrySerializer, CommercialTypeSerializer, PointTypeSerializer, SinonimSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import ReadOnly, MyPermission

# ViewSets define the view behavior.
class PointViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Point.objects.prefetch_related('pointType', 'commercialType')
    serializer_class = PointSerializer

class ExportCountriesViewSet(viewsets.ModelViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [MyPermission]
    queryset = ExportCountry.objects.all()
    serializer_class = ExportCountrySerializer

class CommercialTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [MyPermission]
    queryset = CommercialType.objects.all()
    serializer_class = CommercialTypeSerializer

class PointTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [MyPermission]
    queryset = PointType.objects.all()
    serializer_class = PointTypeSerializer

class SinonimViewSet(viewsets.ModelViewSet):
    permission_classes = [ReadOnly]
    queryset = Sinonim.objects.all()
    serializer_class = SinonimSerializer