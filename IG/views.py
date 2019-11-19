#from django.shortcuts import render

# Create your views here.

# TemplateView
from django.views.generic import TemplateView

class HelloWorld(TemplateView):
    # To point out which template to render by this view
    template_name = 'test.html'