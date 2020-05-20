from django.db import models
from images.models import Image
from django_extensions.db.fields import AutoSlugField
import uuid

class Portfolio(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=127)
    description = models.TextField()
    slug = AutoSlugField(max_length=127, unique=True, populate_from=['name'])
    modified_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    # link to images
    images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return self.name

    def get_images(self):
        return ", ".join([i.name for i in self.images.all()])
