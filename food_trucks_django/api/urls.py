from django.urls import path
from .views import home, find_food_trucks

urlpatterns = [
    path('', home, name="home"),
    path('find_food_trucks/', find_food_trucks, name="find_food_trucks"),
]