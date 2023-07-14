from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Style
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('styles/',
         ListView.as_view(
             queryset=
             Style.objects.all().order_by("name")[:25],
             template_name="all_styles.html"
            )
         ),
    path('styles/<int:style_id>/', views.detail
         ),
]