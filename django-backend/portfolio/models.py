from django.db import models
from builder.models import Builder
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
import uuid

class Portfolio(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    slug = AutoSlugField(max_length=127, unique=True, populate_from=['name'])
    modified_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_images(self):
        return ", ".join([i.name for i in self.images.all()])
    
    # def get_thubnail_image(self):
    #     all_images = self.images.all()
    #     if all_images.exists():
    #         return all_images[0]
    #     else:
    #         return


    def get_absolute_url(self):
        return reverse(
            "portfolio_detail", kwargs={"slug": self.slug}
        )
    