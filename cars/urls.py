from django.urls import path
from .views import Cars


urlpatterns = [
    path('', Cars, name="cars"),
]