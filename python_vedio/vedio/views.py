from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.db import models

def index(request):
    models.Resources.objects.create(

    )
    return HttpResponse("Hello, world. You're at the polls index.")