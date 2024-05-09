from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello! My name is Sahadat Hossain. THis is second commit")

