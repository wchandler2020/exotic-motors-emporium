from django.urls import path
from .views import Cars, Car_Detail, Search


urlpatterns = [
    path('', Cars, name="cars"),
    path('<int:id>', Car_Detail, name="car_detail"),
    path('search', Search, name="search"),
]