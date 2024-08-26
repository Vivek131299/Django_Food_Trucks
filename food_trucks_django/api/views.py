from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodTruck

# Create your views here.
def home(request):
    return HttpResponse(str(list(FoodTruck.objects.all())))
    # return HttpResponse("Hello")