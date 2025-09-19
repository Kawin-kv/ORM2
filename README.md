# Ex02 Django ORM Web Application
## Date: 19.09.2025
## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM

```
models.py
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
admin.py
from django.contrib import admin # type:ignore
from.models import Car,CarAdmin
admin.site.register(Car,CarAdmin)
```
## OUTPUT

![alt text](<Screenshot 2025-09-19 134705.png>)

## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
