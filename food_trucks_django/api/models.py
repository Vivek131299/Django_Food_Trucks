from django.db import models


class FoodTruck(models.Model):
    locationId = models.BigIntegerField(primary_key=True, blank=True, db_column="locationId")
    applicant = models.TextField(null=True, blank=True, db_column="applicant")
    facility_type = models.TextField(null=True, blank=True, db_column="facilitytype")
    cnn = models.BigIntegerField(null=True, blank=True, db_column="cnn")
    location_description = models.TextField(null=True, blank=True, db_column="locationdescription")
    address = models.TextField(null=True, blank=True)
    blocklot = models.TextField(null=True, blank=True)
    block = models.TextField(null=True, blank=True)
    lot = models.TextField(null=True, blank=True)
    permit = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    food_items = models.TextField(null=True, blank=True, db_column="fooditems")  # Use TextField because it can be long
    x_coordinate = models.FloatField(null=True, blank=True, db_column="x")
    y_coordinate = models.FloatField(null=True, blank=True, db_column="y")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    schedule = models.TextField(null=True, blank=True)  # Use TextField because it can be long
    days_hours = models.TextField(null=True, blank=True, db_column="dayshours")
    noi_sent = models.TextField(null=True, blank=True, db_column="noisent")  # If this field is not present in the CSV, keep it as TextField
    approved = models.TextField(null=True, blank=True)
    received = models.TextField(null=True, blank=True)  # If this field is not present in the CSV, keep it as TextField
    prior_permit = models.BigIntegerField(null=True, blank=True, db_column="priorpermit")
    expiration_date = models.TextField(null=True, blank=True, db_column="expirationdate")
    location = models.TextField(null=True, blank=True)
    fire_prevention_districts = models.BigIntegerField(null=True, blank=True, db_column="Fire Prevention Districts")
    police_districts = models.BigIntegerField(null=True, blank=True, db_column="Police Districts")
    supervisor_districts = models.BigIntegerField(null=True, blank=True, db_column="Supervisor Districts")
    zip_codes = models.TextField(null=True, blank=True, db_column="Zip Codes")  # If this field is not present in the CSV, keep it as TextField
    neighborhoods_old = models.BigIntegerField(null=True, blank=True, db_column="Neighborhoods (old)")

    def __str__(self):
        return f"{self.applicant} - {self.address}"
