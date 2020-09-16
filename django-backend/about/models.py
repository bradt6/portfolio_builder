from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _
# Create your models here.

WEEKDAYS = [
    (1, _("Monday")),
    (2, _("Tuesday")),
    (3, _("Wednesday")),
    (4, _("Thursday")),
    (5, _("Friday")),
    (6, _("Saturday")),
    (7, _("Sunday")),
 ]

 
class OpeningHours(models.Model):
    weekday = models.IntegerField(
        choices=WEEKDAYS,
        unique=True)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

class AboutPage(models.Model):

    name_of_bussiness = models.CharField(max_length=27)
    description = models.TextField()
    # This is ABN (AUS) || UK, Europe and USA.
    business_number = models.CharField(max_length=27)
    #Location Services -> This needs to be converted to geoDjango later on for more accurate point to point access and 
    # richer web app experience
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    #Contact Number
    phone_number = PhoneNumberField(blank=True)
    #openingHours
    opening_times = models.ManyToManyField(OpeningHours, blank=True)
    #social media information
    instagram = models.URLField(blank=True)
    linkdin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
