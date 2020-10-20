from django.contrib import admin

from .models import Image

from django.contrib.admin import sites

from .views import addManyImages
# admin.site.register(Image)
from django.urls import path

    # path('upload-images/', addManyImages, name='upload-images'),
# class CustomAdminSite(admin.AdminSite):
#     def get_urls(self):
#         urls = super(CustomAdminSite, self).get_urls()
#         custom_urls = [
#             url('/admin/images/image/add/', addManyImages, name="upload-images")
#         ]
#         return urls + custom_urls

class ImagesAdmin(admin.ModelAdmin):
    change_form_template = 'images_templates/admin_template.html'

    def get_urls(self):
        urls = super().get_urls()
        admin_site = self.admin_site
        custom_urls = [
            path('/admin/images/image/add/', self.admin_view(self.addManyImages), name='upload-images'),
        ]
        return urls + custom_urls


admin.site.register(Image, ImagesAdmin)