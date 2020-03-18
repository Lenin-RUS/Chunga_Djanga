from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'password1', 'password2', 'email', 'job')