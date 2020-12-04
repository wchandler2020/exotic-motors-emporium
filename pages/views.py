from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def Home(request):
    teams = Team.objects.all()
    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by("-created_date")

    context = {
        "teams": teams,
        "featured_car": featured_car,
        "all_cars": all_cars,
    }

    return render(request, 'pages/home.html', context)

def About(request):
    teams = Team.objects.all()

    context = {
        "teams": teams
    }
    return render(request, 'pages/about.html', context)

def Services(request):
    return render(request, 'pages/services.html')

def Contact(request):
    return render(request, 'pages/contact.html')
