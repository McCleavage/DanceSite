from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
# Create your views here.


# Delivers registration page, registers user
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/auth')

    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'authentication/register.html', context)


# Delivers login page
def user_login(request):
    return render(request, 'authentication/login.html')


# Logout function
def user_logout(request):
    logout(request)
    return redirect('home')


# Authentication function, send user to home if authenticated
# redirects to login page if not authenticated
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('home'))


# Show user page, deprecated in favour of sending user to homepage instead
def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

