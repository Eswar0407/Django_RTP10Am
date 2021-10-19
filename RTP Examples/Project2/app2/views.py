from django.shortcuts import render
from django.http import HttpResponse
import time


def requestOne(request):
    time.sleep(10)
    return HttpResponse("<h1>I am One</h1>")


def requestTwo(request):
    return HttpResponse("<h1>I am Two</h1>")