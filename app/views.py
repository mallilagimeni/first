from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse

# Create your views here.
def malli(request):
    return HttpResponse('<marquee><h1>FIRST PROJECT</h1></marquee>')

def malli1(request):
    return HttpResponse('<marquee><h2> SECOND PROJECT</h2><marquee>')
