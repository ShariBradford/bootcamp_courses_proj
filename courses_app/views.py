from django.shortcuts import render, redirect,HttpResponse
from .models import *

# Create your views here.
def index(request):
    return HttpResponse('Hi there!')