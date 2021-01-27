from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Car

def Cars(request):
    #vehicles are ordered the date they were saved to the DB
    cars = Car.objects.order_by("-created_date")
    #each tuple contains the value from the respective field, however if the "flat" parameter is True, the returned results are single values, not a tuple
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    paginator = Paginator(cars, 3)
    page = request.GET.get('page')
    #page pagination
    paged_car = paginator.get_page(page)
    context = {
        "cars": paged_car,
        'model_search': model_search,
        'city_search': city_search,
        'state_search': state_search,
        'year_search': year_search,
        'body_style_search': body_style_search
    }
    return render(request, 'cars/cars.html', context)


def Car_Detail(request, id):
    #Calls get() on a given model/DB object, it raises an Http 404 error instead of the built in DoesNotExist exception.
    single_car = get_object_or_404(Car, pk=id)

    #give the Django template access the DB data
    context = {
        'single_car': single_car,
    }
    #single car object is accessible in the car_detail.html
    return render(request, 'cars/car_detail.html', context)

def Search(request):
    #when a search request is made the data will be return by the created_date
    cars = Car.objects.order_by('-created_date')
    # each tuple contains the value from the respective field, however if the "flat" parameter is True, the returned results are single values, not a tuple
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    # if there is a key word in the request keyword
    if 'keyword' in request.GET:
        # keyword variable will be assigned the data passed into the request
        keyword = request.GET['keyword']
        #if keyword is not null
        if keyword:
            #results will be filter based on the keyword
            cars = cars.filter(description__icontains=keyword)
    # if model not null in temple
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            #filter vehicles by filter by model
            cars = cars.filter(model__iexact=model)
    # if city not null in temple
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            #filter vehicles by city location
            cars = cars.filter(city__iexact=city)
    # if state not null in temple
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            #filter vehicles by state location
            cars = cars.filter(state__iexact=state)
    #if year not null in temple
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            #filter vehicles by year
            cars = cars.filter(year__iexact=year)
    # if tranmission not null in temple
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            # filter vehicles filter by tranmission type
            cars = cars.filter(transmission__iexact=transmission)
    # if body style not null in temple
    if 'body_style' in request.GET:
        # add body style to the min_price / max_price variable
        body_style = request.GET['body_style']
        if body_style:
            #filter vehicles by body style
            cars = cars.filter(body_style__iexact=body_style)
    # if minimum or maximum price not null in temple
    if 'min_price' in request.GET:
        # add keywords to the min_price / max_price variable
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        # if max price is not null
        if max_price:
            # filter vehicles by from the lowest price to the highest price
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    context = {
        "cars": cars,
        'model_search': model_search,
        'city_search': city_search,
        'state_search': state_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
    }
    #takes a request and returns the search.html template, context gives templates access to the data in the
    return render(request, 'cars/search.html', context)

