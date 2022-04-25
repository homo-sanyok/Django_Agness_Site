from django import template
from django.core.mail import send_mail
from .. import forms

register = template.Library()

@register.simple_tag()
def sendMail():
    if (forms.sendMailForm.name != None and forms.sendMailForm.email != None and forms.sendMailForm.message != None):
        message = forms.sendMailForm.name + " | " + forms.sendMailForm.email + "\n" + forms.sendMailForm.message
        send_mail(forms.sendMailForm.theme, message, 'sadha.9eneralow@yandex.ru', ['sadha.9eneralow@yandex.ru'])