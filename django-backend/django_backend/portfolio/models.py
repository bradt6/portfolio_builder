from django.db import models
from images.models import Image
from django_extensions.db.fields import AutoSlugField

class Portfolio(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True)
    name = models.CharField(max_length=127)
    description = models.TextField()
    slug = AutoSlugField(max_length=127, unique=True, populate_from=['name'])
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)


    # link to images
    images = models.ManyToManyField(Image)

    

    def __str__(self):
        return self.name
