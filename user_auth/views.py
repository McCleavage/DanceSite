from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
# Create your views here.


def register_user(request):
    """This function is used to deliver the registration page

        :param WSGIRequest request: The web server request

        :returns: The rendered registration page

        :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/auth')

    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'authentication/register.html', context)


def user_login(request):
    """This function is used to deliver the login page

        :param WSGIRequest request: The web server request

        :returns: The rendered login page

        :rtype: HttpResponse
    """
    return render(request, 'authentication/login.html')


def user_logout(request):
    """Logs out user, then returns home page

        :param WSGIRequest request: The web server request

        :returns: The rendered home page

        :rtype: HttpResponseRedirect
    """
    logout(request)
    return redirect('home')


def authenticate_user(request):
    """This function is used to authenticate the user, then redirect to appropriate page

        :param WSGIRequest request: The web server request

        :returns: A redirect to either the login or home page, depending on if authenticated

        :rtype: HttpResponseRedirect
    """
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

