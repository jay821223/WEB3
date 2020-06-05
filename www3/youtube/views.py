from django.shortcuts import render
from django.views.generic import ListView, DetailView
from youtube.models import Youtube
# Create your views here.

class YoutubeLV(ListView):
    model = Youtube

class YoutubeDV(DetailView):
    model = Youtube