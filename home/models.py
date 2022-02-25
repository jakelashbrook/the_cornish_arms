from django.db import models


class Opening(models.Model):
    ''' A model for the opening times '''
    class Meta:
        verbose_name_plural = 'Opening Times'
    
    weekday_open = models.CharField(max_length=12)
    weekday_close = models.CharField(max_length=12)
    weekend_open = models.CharField(max_length=12)
    weekend_close = models.CharField(max_length=12)

    def get_weekday_open(self):
        return self.weekday_open
    
    def get_weekday_close(self):
        return self.weekday_close
    
    def get_weekend_open(self):
        return self.weekend_open
    
    def get_weekend_open(self):
        return self.weekend_close