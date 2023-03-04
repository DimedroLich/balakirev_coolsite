from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>')

def start_page(request):
    return HttpResponse('<h1>Стартовая страница приложения women</h1>')