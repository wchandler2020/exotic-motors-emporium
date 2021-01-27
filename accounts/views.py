from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.
def Login(request):
    # when a user submits a login request this is a POST request, if HttpRequest object == POST:
    if request.method == 'POST':
        # retrieve data from the login form
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # return a success message for 3 seconds, derived from ./included/messages.html
            messages.success(request, 'Successfully logged in.')
            # after sucessful login redirect user to the dashboard.
            return redirect('dashboard')
        else:
            #if user does match what is in the db return error messsage, derived from ./included/messages.html
            messages.error(request, 'Invalid login request, please try again.')
            # after unsuccessful login attempt redirect to login screen
            return redirect('login')
    return render(request, 'accounts/login.html', {})

def Register(request):
    # when a user submits a register request is a POST request, if HttpRequest object == POST :
    if request.method == 'POST':
        #variables are the values passed into the fields in ./templates/accounts/register.html -- accounts/register
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        #check if the password and the confirm password match
        if password == confirm_password:
            #check if the username is being used by an existing user
            if User.objects.filter(username=username).exists():
                #if the user name exist return an error message
                messages.error(request, 'Username already exists.')
                # redirect to the register screen
                return redirect('register')
            else:
                #check to see if the user registration email is already in the db
                if User.objects.filter(email=email).exists():
                    #if the db exist return an error message
                    messages.error(request, 'Email already exists!')
                    #redirect to register
                    return redirect('register')
                else:
                    #variable to
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    #logs a user in, from a html login form. It takes an HttpRequest(request) object and a User object. login() saves the user’s ID a the session, using Django’s session framework.
                    auth.login(request, user)
                    # show the a success message for 3 seconds that they have been logged in
                    messages.success(request, 'Login Successfully!')
                    # redirect to the users dashboard
                    return redirect('dashboard')
                    #save user to database
                    user.save()
                    #return a success message to user
                    messages.success(request, 'User has been registered successfully!')
                    #after the user is saved to database redirect to the login page
                    return redirect('login')
        else:
            #return an error message if the password != confirm_password
            messages.error(request, 'Passwords do not match')
            #redirect to the register page
            return redirect('register')
    else:
        return render(request, 'accounts/register.html', {})

def Logout(request):
    # when a user submits a register request is a POST request, if HttpRequest object == POST :
    if request.method == "POST":
        #the session data for the current request is completely cleaned out
        auth.logout(request)
        # return a success message to user of successfully logout
        messages.success(request, 'Logged out successfully.')
        #redirect to the home screen
        return redirect('home')
        #if the logout fails there will be no success message and the user will be redirected to the home screen
    return redirect('home')

#django decorator to deny to access the dashboard to dashboard => redirected to login screen
@login_required(login_url = 'login')
def Dashboard(request):
    # accessing contact.Models in db => list of user inquiries order by the newest "create_date"
    user_inquiry = Contact.objects.order_by("-create_date").filter(user_id=request.user.id)
    # dictionary - key: variable user in dashboard.html template to loop through the inquiries. value = user_inquiry
    data = {
        'inquiries':user_inquiry,
    }
    # passes data into the dashboard template.
    return render(request, 'accounts/dashboard.html', data)
