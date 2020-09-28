from django.db import models
from django_extensions.db.fields import AutoSlugField
import uuid
from django.urls import reverse
#TODO: Look into File Storage and managing files:
#       https://docs.djangoproject.com/en/3.0/ref/files/storage/
#       https://docs.djangoproject.com/en/3.0/topics/files/
class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=127)
    date = models.DateField()
    image_file = models.ImageField(upload_to="test")
    # Could this be integrated with openCV for ai auto complete
    web_alt = models.CharField(max_length=64)
    created_at = models.DateField(auto_now_add=True, db_index=True)
    last_modified = models.DateTimeField(auto_now=True)
    # slug = models.SlugField(max_length=127)
    slug = AutoSlugField(max_length=127, populate_from=['name'])
    # url = models.URLField()
    # Sercices and porfolio linked here

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
