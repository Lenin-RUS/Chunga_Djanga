from django import forms

class Sinonim_form(forms.Form):
    point_sinonim=forms.CharField(label="Синоним")