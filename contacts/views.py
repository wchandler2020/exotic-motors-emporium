from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def Inquiry(request):
    # if inquiry request if not null && it is POST request
    if request.method == "POST":
        # each tuple contains the value from the respective field, however if the "flat" parameter is True, the returned results are single values, not a tuple
        car_id = request.POST["car_id"]
        car_title = request.POST["car_title"]
        user_id = request.POST["user_id"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        customer_need = request.POST["customer_need"]
        city = request.POST["city"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        #if the user is signed in
        if request.user.is_authenticated:
            #user ID will be assigned to the contact users ID
            user_id = request.user.id
            #returns a tuple with user ID and the ID of the car to determine if a users has already made an inquirie on this specific vehicle
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            # check if the user has already made an inquirie.
            if has_contacted:
                #return a message to let the user know a let the user know that they have already made an inquiry on this vehicle
                messages.error(request, "You have already made an inquery about this vehicle, someone will contact you soon in reference to your inquery.")
                #redirect the user to the vehicle's detail page
                return redirect(f"/cars/{car_id}")
        #contact information is added to the DB
        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name,
                          customer_need=customer_need, city=city, email=email, phone=phone, message=message)
        #looks for the superuser information
        admin_info = User.objects.get(is_superuser=True)
        #superuser email information.
        admin_email = admin_info.email
        #Mail is sent using the SMTP host and port specified in the EMAIL_HOST and EMAIL_PORT in settings. The EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in settings.
        send_mail(
            'New Customer Inquiry',
            'You have a new inquiry for the car ' + car_title + '. Please login to your admin panel for more info.',
            'j.boylston77@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        # save user email to the DB
        contact.save()
        #send a success message to the customer
        messages.success(request, "Thank you for your inquiry, someone will contact you shortly.")
        #redirect the customer back to the vehicle description page.
        return redirect(f"/cars/{car_id}")
