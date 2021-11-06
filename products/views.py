from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def cart(request):
    return render(request, 'cart.html', {})


def checkout(request):
    return render(request, 'checkout.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def shopsingle(request):
    return render(request, 'shopsingle.html', {})


def shop(request):
    return render(request, 'shop.html', {})


def thankyou(request):
    return render(request, 'thankyou.html', {})


# Login
def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        print(name, email, password)
        user = auth.authenticate(username=name,
                                 useremail=email,
                                 password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,
                          'invalid info please make sure username & password')
            return redirect('/signup')
    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/')


# signup
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        print(name, email, password)
        user = User.objects.create_user(username=name,
                                        email=email,
                                        password=password)
        user.save()
        return redirect('/login')
    # return render(request, 'account.html')
