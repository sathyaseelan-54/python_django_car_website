from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Booking

class Index(TemplateView):
    model = Booking
    template_name = 'index.html'


class About(TemplateView):
    model = Booking
    template_name = 'about.html'


class Servies(TemplateView):
    model = Booking
    template_name = 'servies.html'


class Contact(TemplateView):
    model = Booking
    template_name = 'contact.html'



