from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Bus(BaseModel):
    bus_number = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100)
    no_of_seats = models.PositiveIntegerField(null=True, blank=True)
    trip = models.CharField(max_length=100)
    duration = models.CharField(max_length=50, null=True, blank=True)
    conductor = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
