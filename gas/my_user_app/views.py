from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .forms import RegistrationForm
from django.views.generic import CreateView
from .models import MyUser

# Create your views here.
class UserLoginView(LoginView):
    template_name = 'my_user_app/login.html'

class UserCreateView(CreateView):
    model = MyUser
    template_name = 'my_user_app/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')