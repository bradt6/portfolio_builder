from django.contrib import admin

from .models import Image

from django.contrib.admin import sites

# admin.site.register(Image)

class ImagesAdmin(admin.ModelAdmin):
    change_form_template = 'images_templates/admin_template.html'
# class ImagesAdmin(admin.ModelAdmin):
#     change_form_template = 'images_templates/admin_template.html'

admin.site.register(Image, ImagesAdmin)
# custom_admin_site.register(Image, ImagesAdmin)