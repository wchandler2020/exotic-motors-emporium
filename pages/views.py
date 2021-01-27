from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib import messages

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
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        email_subject = f"New website message in reference to: {subject}"
        message_body = f"Name: {name}\n Email: {email}\n Phone Number: {phone}\n Message: {message}"
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            email_subject,
            message_body,
            'j.boylston77@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, "Thank you for contacting us, someone will be in contact with you soon.")
        return redirect('contact')
    return render(request, 'pages/contact.html')
