from django.urls import path
from . import views
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Contact

urlpatterns = [
    path('', views.index, name='home'),
    path('about_us', views.about_us, name="about_us"),
    path('contact', views.contact, name="contact"),
    path('success', views.success, name="success"),
    path('newsletter', views.newsletter, name="newsletter"),
    path(
     'success_newsletter',
     views.success_newsletter,
     name="success_newsletter"),
]
