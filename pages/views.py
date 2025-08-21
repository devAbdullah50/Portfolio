from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'
class About(TemplateView):
    template_name = 'about.html'
class Projects(TemplateView):
    template_name = 'projects.html'
class Services(TemplateView):
    template_name = 'services.html'
class Contact(TemplateView):
    template_name = 'contact.html'