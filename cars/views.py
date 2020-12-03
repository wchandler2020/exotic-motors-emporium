from django.shortcuts import render

def Cars(request):
    return render(request, 'cars/cars.html')
