from django import forms
from .models import *

class sendMailForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control", "id":"name", "placeholder":"ФИО"}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control", "type":"email", "id":"email", "placeholder":"Email"}))
    theme = forms.CharField(label='', widget=forms.TextInput(attrs={"class":"form-control", "id":"subject", "placeholder":"Тема"}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={"class":"form-control", "name":"message", "placeholder":"Описание проблемы", "rows":"5"}))