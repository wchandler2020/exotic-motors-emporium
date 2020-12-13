from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def Home(request):
    teams = Team.objects.all()
    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by("-created_date")
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    context = {
        "teams": teams,
        "featured_car": featured_car,
        "all_cars": all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'state_search': state_search,
        'year_search': year_search,
        'body_style_search': body_style_search
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
