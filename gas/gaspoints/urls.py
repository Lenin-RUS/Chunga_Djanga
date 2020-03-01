from django.urls import path
from gaspoints import views

app_name='gaspoints'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('add_name/', views.add_name, name='add_name'),
    path('point/<int:id>/', views.point, name='point')
]

