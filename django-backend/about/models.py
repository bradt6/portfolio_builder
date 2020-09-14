from django.db import models

# Create your models here.
class AboutPage(models.Model):

    name_of_bussiness = models.Charfield()
    description = models.Textfield()
    # This is ABN (AUS) || UK, Europe and USA.
    business_number = models.Charfield()
    #Location Services
    lat = models.DecimalField(_('Latitude'), max_digits=10, decimal_places=8)
    lng = models.DecimalField(_('Longitude'), max_digits=11, decimal_places=8)

