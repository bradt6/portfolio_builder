from django.db import models

# Create your models here.
class AboutPage(models.Model):

    name_of_bussiness = models.CharField(max_length=27)
    description = models.TextField()
    # This is ABN (AUS) || UK, Europe and USA.
    business_number = models.CharField(max_length=27)
    #Location Services
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)

