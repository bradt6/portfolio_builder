from django.db import models
from django_extensions.db.fields import AutoSlugField
import uuid

from builder.models import Builder

class Service(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    slug = AutoSlugField(max_length=63, populate_from=['name'])

    def __str__(self):
        return self.name
