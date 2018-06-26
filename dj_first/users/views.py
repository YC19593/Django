from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo

# Create your views here.


def index(request):
    """index视图函数"""
    return HttpResponse("hello the world!")