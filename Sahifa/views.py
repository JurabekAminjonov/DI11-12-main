from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class SahifaPageView(TemplateView):
    template_name='sahifa.html'