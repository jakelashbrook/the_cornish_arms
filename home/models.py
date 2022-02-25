from django.db import models


class Opening(models.Model):
    ''' A model for the opening times '''
    class Meta:
        verbose_name_plural = 'Opening Times'
    
    monday = models.CharField(max_length=12, default='timezone.now')
    tuesday = models.CharField(max_length=12, default='timezone.now')
    wednesday = models.CharField(max_length=12, default='timezone.now')
    thursday = models.CharField(max_length=12, default='timezone.now')
    friday = models.CharField(max_length=12, default='timezone.now')
    saturday = models.CharField(max_length=12, default='timezone.now')
    sunday = models.CharField(max_length=12, default='timezone.now')

    def get_monday(self):
        return self.monday
    
    def get_tuesday_close(self):
        return self.tuesday
    
    def get_wednesday(self):
        return self.wednesday
    
    def get_thursday(self):
        return self.thursday
    
    def get_friday(self):
        return self.friday

    def get_saturday(self):
        return self.saturday

    def get_sunday(self):
        return self.sunday


class Food(models.Model):
    ''' The food service hours '''

    class Meta:
        verbose_name_plural = 'Food Times'

    monday = models.CharField(max_length=12, default='timezone.now')
    tuesday = models.CharField(max_length=12, default='timezone.now')
    wednesday = models.CharField(max_length=12, default='timezone.now')
    thursday = models.CharField(max_length=12, default='timezone.now')
    friday = models.CharField(max_length=12, default='timezone.now')
    saturday = models.CharField(max_length=12, default='timezone.now')
    sunday = models.CharField(max_length=12, default='timezone.now')
    if_lunch = models.BooleanField(default=False)
    lunch_hours = models.CharField(max_length=12, default='timezone.now')

    def get_monday(self):
        return self.monday
    
    def get_tuesday_close(self):
        return self.tuesday
    
    def get_wednesday(self):
        return self.wednesday
    
    def get_thursday(self):
        return self.thursday
    
    def get_friday(self):
        return self.friday

    def get_saturday(self):
        return self.saturday

    def get_sunday(self):
        return self.sunday

    def get_lunch_hours(self):
        return self.lunch_hours
