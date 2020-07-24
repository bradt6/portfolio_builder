from django.db import models
from images.models import Image
from builder.models import Builder
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
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
    # link to the builder
    builder = models.ForeignKey(Builder, on_delete=models.SET_DEFAULT, default=None)

    def __str__(self):
        return self.name

    def get_images(self):
        return ", ".join([i.name for i in self.images.all()])


    def get_absolute_url(self):
        return reverse(
            "portfolio_detail", kwargs={"slug": self.slug}
        )
    
    def get_pageManager(self):
        return self.builder.pageManager
    
    def get_template(self):
        return self.builder.template



