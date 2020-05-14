from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=128)
    email_address = models.EmailField()
    mobile_number = PhoneNumberField()
