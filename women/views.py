from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Страница приложения women')

def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>')

def start_page(request):
    return HttpResponse('<h1>Стартовая страница</h1>')