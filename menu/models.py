from django.db import models

# Create your models here.
class MenuItem(models.Model):
    ''' Items on the food menu '''
    dish_title = models.CharField(max_length=125, null=False, blank=False)
    dish_description = models.CharField(max_length=250, null=False, blank=False)
    allergens = models.CharField(max_length=120, null=True, blank=True)
    is_gluten_free = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    dish_price = models.IntegerField(null=False, blank=False)