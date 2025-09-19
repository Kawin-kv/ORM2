from django.db import models # type:ignore
from django.contrib import admin # type:ignore
class Car(models.Model):
    car_name= models.CharField()
    car_model = models.CharField()
    car_release_date = models.DateField()
    car_millage = models.IntegerField()
    car_color = models.CharField()

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_model', 'car_release_date', 'car_millage','car_color')
