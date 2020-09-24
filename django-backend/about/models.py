from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _

from images.models import Image
# Create your models here.
from contacts.forms import ContactForm
from contacts.models import Contact
from django.shortcuts import render

WEEKDAYS = [
    (1, _("Monday")),
    (2, _("Tuesday")),
    (3, _("Wednesday")),
    (4, _("Thursday")),
    (5, _("Friday")),
    (6, _("Saturday")),
    (7, _("Sunday")),
 ]

SOCIAL_PLATFORM = [
     (1, _("Facebook")),
     (2, _("Instagram")),
     (3, _("Twitter")),
     (4, _("Youtube")), 
     (5, _("Linkedin")),
 ]
SOCIAL_HTML_TAGS = [
    "fa fa-facebook",
    "fa fa-instagram",
    "fa fa-twitter",
    "fa fa-youtube", 
    "fa fa-linkedin"
]

# def contact_create(request):
#     if request.method =='POST':
#         contact_form = ContactForm(data=request.POST)
#         if contact_form.is_valid():
#             new_contact = contact_form.save()
#     else:
#         contact_form = ContactForm()
#     return render(request, 'contact_me/base.html',  {'new_contact': new_contact, 'contact_form': contact_form})
        


 
class OpeningHours(models.Model):
    weekday = models.IntegerField(
        choices=WEEKDAYS,
        unique=True)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

class SocialMediaAccount(models.Model):
    account_name = models.IntegerField(
        choices=SOCIAL_PLATFORM)
    account_url = models.URLField()
    # icon = models.OneToOneField(Image, on_delete=models.CASCADE, blank=True)
    social_icon = models.CharField(max_length=30, editable=False)

    def save(self, *args, **kwargs):
        self.social_icon = SOCIAL_HTML_TAGS[int(self.account_name)-1]
        super(SocialMediaAccount, self).save(*args, **kwargs)

class AboutPage(models.Model):

    name_of_bussiness = models.CharField(max_length=27)
    description = models.TextField()
    # This is ABN (AUS) || UK, Europe and USA.
    business_number = models.CharField(max_length=27)
    #License Number -> this is seperate from business number. Certain trades need this to do jobs over a certain price
    license_number = models.CharField(max_length=27, blank=True)
    #Location Services -> This needs to be converted to geoDjango later on for more accurate point to point access and 
    # richer web app experience
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    #Contact Number
    phone_number = PhoneNumberField(blank=True)
    #openingHours
    opening_times = models.ManyToManyField(OpeningHours, blank=True)
    #social media information
    social_accounts = models.ManyToManyField(SocialMediaAccount, blank=True)


