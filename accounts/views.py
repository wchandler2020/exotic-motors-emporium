from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login request, please try again.')
            return redirect('login')
    return render(request, 'accounts/login.html', {})

def Register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    auth.login(request, user)
                    messages.success(request, 'Login Successfully!')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'User has been registered successfully!')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html', {})

def Logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'Logged out successfully.')
        return redirect('home')
    return redirect('home')

def Dashboard(request):
    return render(request, 'accounts/dashboard.html', {})
