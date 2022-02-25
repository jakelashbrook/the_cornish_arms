from django.db import models

# Create your models here.

class Table(models.Model):
    ''' Tables within the business '''
    table_number = models.IntegerField(blank=False, null=False)
    number_of_Seats = models.IntegerField(blank=False, null=False)
    if_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class TableBooking(models.Model):
    ''' Table Booked '''
    full_name = models.CharField(max_length=50, blank=False, null=False)
    email_address = models.EmailField(blank=False, null=False)
    phone_number = models.IntegerField(blank=False, null=False)
    number_of_guests = models.IntegerField(blank=False, null=False)
    date_of_booking = models.DateField(blank=False, null=False)
    time_of_booking = models.TimeField(blank=False, null=False)
    special_requests = models.TextField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name