from django.db import models

# Create your models here.

class Table(models.Model):
    ''' Tables within the business '''
    table_number = models.IntegerField(blank=False, null=False)
    number_of_seats = models.IntegerField(blank=False, null=False)
    if_available = models.BooleanField(default=True)
    booking_info = models.ManyToManyField('Booking')


class Booking(models.Model):
    ''' Table Booked '''
    booking_id = models.CharField(max_length=124)
    full_name = models.CharField(max_length=50, blank=False, null=False)
    email_address = models.EmailField(blank=False, null=False)
    phone_number = models.DecimalField(max_digits=11, decimal_places=0,blank=False, null=False)
    number_of_guests = models.IntegerField(blank=False, null=False)
    date_of_booking = models.DateField(blank=False, null=False)
    time_of_booking = models.TimeField(blank=False, null=False)
    special_requests = models.TextField(max_length=150, null=True, blank=True)
    deposit_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Service(models.Model):
    ''' Service hours '''
    lunch_start = models.TimeField()
    lunch_end = models.TimeField()
    dinner_start = models.TimeField()
    dinner_end = models.TimeField()
