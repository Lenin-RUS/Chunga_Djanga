from django import forms
from .models import Point

class Sinonim_form(forms.Form):
    point_sinonim=forms.CharField(label="Синоним")

class SendMail(forms.Form):
    name=forms.CharField(label='Имя')
    email=forms.EmailField(label='Адрес почты')
    phone=forms.CharField(label='Телефон')
    message=forms.CharField(label='Сообщение')

class Add_point(forms.ModelForm):
    class Meta:
        model=Point
        fields='__all__'