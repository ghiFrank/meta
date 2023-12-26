from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from datetime import datetime

def welcome(request):
    content = "<html><body><h1>Welcome</h1></body></html>"
    return HttpResponse(content)

def home(request):
    path = request.path
    return HttpResponse(path, content_type='text/html', charset='utf-8')

def date(request):
    content = datetime.today().year
    return HttpResponse(content)

def menu(request):
    text = """<h1 style="color: #F4CE14;"> TEST WITH COLOR</h1>"""
    return HttpResponse(text)