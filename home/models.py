from django.db import models


class OpeningTime(models.Model):
    ''' Set the Opening Times Model '''
    class Meta:
        verbose_name_plural = ' Opening Times'


    weekday_opening = models.CharField(max_length=10, null=False, blank=False)
    weekday_closing = models.CharField(max_length=10, null=False, blank=False)
    weekend_opening = models.CharField(max_length=10, null=False, blank=False)
    weekend_closing = models.CharField(max_length=10, null=False, blank=False)

class FoodTime(models.Model):
    ''' Food service hours '''
    class Meta:
        verbose_name_plural = ' Food Times'


    lunch_start = models.CharField(max_length=10, null=False, blank=False)
    lunch_end = models.CharField(max_length=10, null=False, blank=False)
    dinner_start = models.CharField(max_length=10, null=False, blank=False)
    dinner_end = models.CharField(max_length=10, null=False, blank=False)

class Event(models.Model):
    ''' To publish events being held '''
    class Meta:
        verbose_name_plural = ' Events'


    event_name = models.CharField(max_length=20, null=True, blank=True)
    event_day = models.CharField(max_length=20, null=True, blank=True)
    event_time = models.CharField(max_length=20, null=True, blank=True)
    event_info = models.TextField(max_length=300, null=True, blank=True)
    event_image = models.ImageField(default=0)