from django.urls import path
from my_user_app import views
from django.contrib.auth.views import LogoutView

app_name='my_user_app'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.UserCreateView.as_view(), name='register'),
]

