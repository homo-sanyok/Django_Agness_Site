from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('services/', views.services),
    path('team/', views.team),
    path('contact/', views.contact),
]
