from django.contrib import admin
from .models import OpeningTime, FoodTime, Event
# Register your models here.


admin.site.register(OpeningTime)
admin.site.register(FoodTime)
admin.site.register(Event)