"""gas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from gaspoints.api_views import PointViewSet, ExportCountriesViewSet, CommercialTypeViewSet, PointTypeViewSet, SinonimViewSet, SelectedPoints

router = routers.DefaultRouter()
router.register(r'Points', PointViewSet)
router.register(r'Export_Countries', ExportCountriesViewSet)
router.register(r'Commercial_Types', CommercialTypeViewSet)
router.register(r'Point_Types', PointTypeViewSet)
router.register(r'Sinonims', SinonimViewSet)
# router.register(r'Sin_points', PointAPIView.as_view(), basename='Sin_points')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gaspoints.urls', namespace='gas')),
    path('users/', include('my_user_app.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v0/', include(router.urls)),
    path('SelPoints/<str:point>/', SelectedPoints.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        ] + urlpatterns