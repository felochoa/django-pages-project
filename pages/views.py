from django.shortcuts import render
from django.views.generic import TemplateView #built in view to display our template

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"
    
