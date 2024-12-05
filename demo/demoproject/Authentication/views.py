from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login')
        else:
            login(request, user)
            return redirect('home')

    return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name')
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username already exists
        if User.objects.filter(username=user_name).exists():
            messages.info(request, 'Username already exists')
            return redirect('/signup')

        # Create the user
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=user_name
        )
        user.set_password(password)
        user.save()
        messages.info(request, 'Account Created Successfully')

        return redirect('/login')

    return render(request, "signup.html")

def home(request):
    return render(request, "home.html")

def logout_page(request):
    logout(request)
    return redirect('login')
