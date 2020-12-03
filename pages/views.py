from django.shortcuts import render
from .models import Team

# Create your views here.
def Home(request):
    teams = Team.objects.all()

    context = {
        "teams": teams,
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
