from django.db import models

# Create your models here.
class MenuItem(models.Model):
    ''' Items on the food menu '''
    dish_title = models.CharField(max_length=125, null=False, blank=False)
    dish_description = models.TextField()
    allergens = models.CharField(max_length=120, null=True, blank=True)
    is_gluten_free = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    dish_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name