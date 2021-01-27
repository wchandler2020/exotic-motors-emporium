from django.urls import path
from .views import Cars, Car_Detail, Search


urlpatterns = [
    #path to see all the vehicles in the DB
    path('', Cars, name="cars"),
    #path to see a single vehicle description based on the vehicles ID
    path('<int:id>', Car_Detail, name="car_detail"),
    #path where search results will be return to this view
    path('search', Search, name="search"),
]