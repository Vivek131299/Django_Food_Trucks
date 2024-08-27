from django.shortcuts import render
from django.http import JsonResponse
from .models import FoodTruck
from geopy.distance import geodesic
from django.conf import settings


def home(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, "home.html", context)


def find_food_trucks(request):
    lat = float(request.GET.get('lat'))
    lng = float(request.GET.get('lng'))
    print(lat, lng)
    clicked_location = (lat, lng)

    food_trucks = []
    for truck in FoodTruck.objects.all():
        truck_location = (truck.latitude, truck.longitude)
        distance = geodesic(clicked_location, truck_location).km

        food_trucks.append({
            'applicant': truck.applicant,
            'latitude': truck.latitude,
            'longitude': truck.longitude,
            'address': truck.address,
            'status': truck.status,
            'facility_type': truck.facility_type,
            'schedule': truck.schedule,
            'distance': distance})

    food_trucks = sorted(food_trucks, key=lambda x: x['distance'])[:5]

    return JsonResponse(food_trucks, safe=False)
