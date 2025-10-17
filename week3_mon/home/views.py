from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse("Hey Gaurav Here learning Django")

def Student(request):
    return