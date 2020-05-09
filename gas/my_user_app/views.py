from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from rest_framework.authtoken.models import Token
from .forms import RegistrationForm
from django.views.generic import CreateView, DetailView
from .models import MyUser, Place_of_job


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'my_user_app/login.html'

class UserCreateView(CreateView):
    model = MyUser
    template_name = 'my_user_app/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')

class UserDetailView(DetailView):
    model = MyUser
    template_name = 'my_user_app/profile.html'


def update_token(request):
    user = request.user
    try:
        user.auth_token.delete()
    except:
        pass
    Token.objects.create(user=user)
    return HttpResponseRedirect(reverse('users:profile', kwargs={'pk': user.pk}))