from django.urls import path
from gaspoints import views

app_name='gaspoints'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('add_point/', views.add_point, name='add_point'),
    path('point/<int:id>/', views.point, name='point'),
    path('send_mail/', views.send_mail, name='send_mail'),
    path('point_list/', views.PointListView.as_view(), name='point_list'),
    path('point_detail/<int:pk>/', views.PointDetailView.as_view(), name='point_detail'),
    path('point_update/<int:pk>/', views.PointUpdateView.as_view(), name='point_update'),
    path('point_delete/<int:pk>/', views.PointDeleteView.as_view(), name='point_delete'),
    path('new_point/', views.PointCreateView.as_view(), name='new_point'),

]

