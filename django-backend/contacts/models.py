from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    name = models.CharField(max_length=128)
    email_address = models.EmailField()
    mobile_number = PhoneNumberField()
    created_at = models.DateField(auto_now_add=True, editable=False)
    description_of_job = models.TextField()


    def __str__(self):
        return self.name

