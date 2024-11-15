from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from app.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.hashers import check_password
# Create your views here.


def Welcome_page(request):
    return render(request, 'index.html')  

@never_cache
def home(request):
    if 'email' in request.session:
        email = request.session["email"]
        try:
            person = People.objects.get(email=email)
            coffee = Coffee.objects.all()
            # Combine the two dictionaries into one
            context = {
                "person_name": person.username,
                "coffee": coffee
            }
            return render(request, 'home.html', context)
        except People.DoesNotExist:
            # Handle case where the user does not exist
            return redirect('login')
    return redirect('login')

# def home(request):
#     coffee = Coffee.objects.all()
#     return render(request,"home.html",{'coffee':coffee})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        # Check if passwords match
        if password == confirm_password:
            # Create a new People instance with hashed password
            user = People(
                username=username,
                email=email,
                password=make_password(password)  # Hashing the password
            )
            user.save()
            return redirect('login')  # Redirect to login page after successful signup

    return render(request, 'signup.html')  

@never_cache
def login(request):
    if 'username' in request.session:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Attempt to get the user from the People model
        try:
            user = People.objects.get(email=email)
        except People.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html')

        # Check if the password matches using check_password
        if user and check_password(password, user.password):
            request.session['email'] = email
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('login')