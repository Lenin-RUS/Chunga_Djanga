from django.contrib import admin
from .models import Point, CommercialType, PointType

admin.site.register(Point)
admin.site.register(CommercialType)
admin.site.register(PointType)
