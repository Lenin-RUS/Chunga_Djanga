from django import forms
from .models import Point, Sinonim

class Add_sinonim(forms.ModelForm):
    class Meta:
        model=Sinonim
        # fields='__all__'
        exclude = ('user', 'root_point')

class SendMail(forms.Form):
    name=forms.CharField(label='Имя')
    email=forms.EmailField(label='Адрес почты')
    phone=forms.CharField(label='Телефон')
    message=forms.CharField(label='Сообщение')

class Add_point(forms.ModelForm):
    class Meta:
        model=Point
        exclude = ('user', )
        # fields='__all__'


class NewPoint(forms.Form):
    class Meta:
        model=Point
        exclude = ('user', )