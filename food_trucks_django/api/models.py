from django.db import models


class FoodTruck(models.Model):
    locationId = models.IntegerField(null=True, blank=True)
    applicant = models.TextField(null=True, blank=True)
    facility_type = models.TextField(null=True, blank=True)
    cnn = models.IntegerField(null=True, blank=True)
    location_description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    blocklot = models.TextField(null=True, blank=True)
    block = models.TextField(null=True, blank=True)
    lot = models.TextField(null=True, blank=True)
    permit = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    food_items = models.TextField(null=True, blank=True)
    x_coordinate = models.FloatField(null=True, blank=True)
    y_coordinate = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    schedule = models.TextField(null=True, blank=True)
    days_hours = models.TextField(null=True, blank=True)
    noi_sent = models.TextField(null=True, blank=True)
    approved = models.TextField(null=True, blank=True)
    received = models.TextField(null=True, blank=True)
    prior_permit = models.IntegerField(null=True, blank=True)
    expiration_date = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    fire_prevention_districts = models.IntegerField(null=True, blank=True)
    police_districts = models.IntegerField(null=True, blank=True)
    supervisor_districts = models.IntegerField(null=True, blank=True)
    zip_codes = models.TextField(null=True, blank=True)
    neighborhoods_old = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.applicant} - {self.address}"
