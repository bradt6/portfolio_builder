from django.db import models
from django_extensions.db.fields import AutoSlugField

class Image(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=127)
    date = models.DateField()
    image_file = models.ImageField()
    web_alt = models.CharField(max_length=64)
    last_modified = models.DateTimeField(auto_now=True)
    # slug = models.SlugField(max_length=127)
    slug = AutoSlugField(max_length=127, populate_from=['name'])


    # Sercices and porfolio linked here
    

