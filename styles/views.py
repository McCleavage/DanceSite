from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Style


def index(request):
    """This function is used to render the index page of the dances

        :param WSGIRequest request: The web server request
        :returns: The rendered index page

        :rtype: HttpResponse
    """
    return render(request, "index.html")


def detail(request, style_id):
    """This function is used to render views of individual dance pages to authenticated users
        or redirect to login page otherwise

        :param WSGIRequest request: The web server request
        :param int style_id: The id of the style requested
        :returns: A redirect to either the login or home page, depending on if authenticated

        :rtype: HttpResponse
    """
    if request.user.is_authenticated:
        style = get_object_or_404(Style, pk=style_id)
        return render(request, "style.html", {'style': style})
    else:
        return redirect(reverse("user_auth:login"))