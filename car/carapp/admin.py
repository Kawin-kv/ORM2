from django.contrib import admin # type:ignore
from.models import Car,CarAdmin
admin.site.register(Car,CarAdmin)