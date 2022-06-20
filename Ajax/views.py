from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import User
# Create your views here.

def index(reques):
    modal = User.objects.all()
    return render(reques, 'polls/starter.html', context={'data': modal})
