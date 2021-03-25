from django.db import models
from django_extensions.db.fields import AutoSlugField
import uuid
from django.urls import reverse
#TODO: Look into File Storage and managing files:
#       https://docs.djangoproject.com/en/3.0/ref/files/storage/
#       https://docs.djangoproject.com/en/3.0/topics/files/
from django.utils.html import mark_safe
from portfolio.models import Portfolio
from services.models import Service

def create_path(instance, filename):
    return f"images/{instance.name}/{filename}"

# class ServicesImage(models.Model):
#     name = models.CharField(max_length=127)
#     image_file = models.ImageField(upload_to="images/services/")
#     created_at = models.DateField(auto_now_add=True, db_index=True)
#     last_modified = models.DateTimeField(auto_now=True)
#     slug = AutoSlugField(max_length=127, populate_from=['name'])
#     service = models.ForeignKey(Service, related_name="images")

#     def get_thumbnail(self):
#         return self.images.filter(default=True).first()
class PortfolioImage(models.Model):
    name = models.CharField(max_length=127)
    image_file = models.ImageField(upload_to="images/portfolio/")
    created_at = models.DateField(auto_now_add=True, db_index=True)
    last_modified = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(max_length=127, populate_from=['name'])
    portfolio = models.ForeignKey(Portfolio, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])

    def image_tag(self):
            return mark_safe('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.image_file.url))
    
    def get_thumbnail(self):
        return self.images.filter(default=True).first()