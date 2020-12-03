from django.contrib import admin
from django.urls import path
from .views import Home, About, Services, Contact

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('services/', Services, name='services'),
    path('contact/', Contact, name='contact')
]
