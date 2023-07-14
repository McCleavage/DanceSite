from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Style
# Create your views here.
def index(request):
    return render(request, "index.html")

# Locks viewing of individual dance pages to logged-in users
def detail(request, style_id):
    if request.user.is_authenticated:
        style = get_object_or_404(Style, pk=style_id)
        return render(request, "style.html", {'style': style})
    else:
        return redirect(reverse("user_auth:login"))