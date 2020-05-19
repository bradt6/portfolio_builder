from django.db import models
from images.models import Image
from django_extensions.db.fields import AutoSlugField
import uuid

class Service(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=63)
    description = models.TextField()
    # slug = models.SlugField(max_length=63, unique=True)
    created_at = models.DateField(auto_now_add=True)
    slug = AutoSlugField(max_length=63, populate_from=['name'])  
    # link to image class
    image = models.ForeignKey(Image, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
