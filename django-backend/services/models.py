from django.db import models
from images.models import Image
from django_extensions.db.fields import AutoSlugField
import uuid

from builder.models import Builder

class Service(models.Model):
    # id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=63)
    description = models.TextField()
    # slug = models.SlugField(max_length=63, unique=True)
    created_at = models.DateField(auto_now_add=True)
    slug = AutoSlugField(max_length=63, populate_from=['name'])
    # link to image class
    # image = models.ForeignKey(Image, on_delete=models.DO_NOTHING, blank=True, null=True)

    # TODO There is an issue with adding the images: if this isnt here it
    # works however it does link back to the correctly
    main_image = models.ForeignKey(
               Image,
               on_delete=models.SET_NULL,
               null=True,
               blank=True,
           )

    def __str__(self):
        return self.name

#    def check_if_image(self):
#        return len(self.image) > 0
#
#    def get_image(self):
#        if check_if_image:
#            return self.image[0]
#        return

# class ServicesImage(models.Model):
#     image = models.ImageField(blank=True, null=True)
#     service = models.ForeignKey(Service, related_name = 'image', on_delete=models.DO_NOTHING)

