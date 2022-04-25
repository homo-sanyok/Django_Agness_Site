from django.shortcuts import render, redirect
from .forms import *
from django.core.mail import send_mail

def index(request):
    return render(request, 'moderna/index.html')

def about(request):
    return render(request, 'moderna/about.html')

def services(request):
    return render(request, 'moderna/services.html')

def team(request):
    return render(request, 'moderna/team.html')

def contact(request):
    form = sendMailForm()

    if (request.method == 'POST'):
        contact_form = sendMailForm(request.POST)
        if (contact_form.is_valid()):
            message = contact_form.cleaned_data['name'] + " | " + contact_form.cleaned_data['email'] + "\n" + contact_form.cleaned_data['message']
            send_mail(contact_form.cleaned_data['theme'], message, 'sadha.9eneralow@yandex.ru', ['sadha.9eneralow@yandex.ru'])
            return redirect(request.path)

    return render(request, 'moderna/contact.html', {'form': form})
