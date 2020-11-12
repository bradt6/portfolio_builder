from django.contrib import admin

from .models import Image

from django.contrib.admin import sites

from django.urls import path
from django.conf.urls import url 

from django.shortcuts import render
from django.template.response import TemplateResponse
from .views import addManyImages

# from .views import AddManyImages 

from django.urls import reverse
from django.utils.safestring import mark_safe

def upload_images():
    url = reverse('image:upload-images')
    return mark_safe(f'<a href="{url}">View</a>')
@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    # change_form_template = "admin/admin_template.html"
    def get_urls(self):
        urls = super(ImagesAdmin, self).get_urls()
        my_url = [url('admin/image/upload-images', self.admin_site.admin_view(addManyImages))]
        return urls + my_url