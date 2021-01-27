from django.urls import path
from .views import Login, Register, Logout, Dashboard

urlpatterns = [
    #url for customer login
    path('login', Login, name='login'),
    #url for a customer to register
    path('register', Register, name='register'),
    #url for customer logout
    path('logout', Logout, name='logout'),
    #url for customer dashboard
    path('dashboard', Dashboard, name='dashboard'),
]