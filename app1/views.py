from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
# Create your views here.

def task1(request):
    return HttpResponse("This is task 1")

def task2(request):
    return HttpResponse("This is task 2")