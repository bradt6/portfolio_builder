from django.contrib import admin

from .models import Image

from django.contrib.admin import sites

from django.urls import path
from django.conf.urls import url 

from django.shortcuts import render
from django.template.response import TemplateResponse
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin #and these
from django.http import HttpResponse
from .views import addManyImages 

from django.urls import reverse
from django.utils.safestring import mark_safe

from django.forms import ModelForm

from django.http.response import JsonResponse


# def upload_images():
#     url = reverse('image:upload-images')
#     return mark_safe(f'<a href="{url}">View</a>')

class ImageAdminForm(ModelForm):
    class Meta:
        model = Image
        fields = ["name"]


class ImagesAdmin(admin.ModelAdmin):
    change_form_template = "admin/admin_template.html"
    # add_form_template = "admin/admin_template.html"
    # form = ImageAdminForm
    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['your_custom_data'] = self.addManyImages2(request)
        return super().add_view(request, form_url, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        my_url = [path('many1/', self.admin_site.admin_view(self.addManyImages2)),
                  path('many2/', addManyImages),]
        new_urls = my_url + urls
        print(new_urls)
        return new_urls

    def addManyImages2(self, request):
        print("ENTERING METHOD HERE")
        # if request.method == "GET":
        #     return TemplateResponse(request,'admin/admin_template.html') 
        
        if request.method == "POST":
            print("HERE")
            print("REQUEST:", request)
            name = request.POST.get('name')
            length = request.POST.get('length')
            print("LENGTH :", length)

            count = 0
            for file_num in range(0, int(length)):
                Image.objects.create(
                    name=f"{name}_{count}",
                    image_file=request.FILES.get(f"images{file_num}")
                )
                # return JsonResponse({'name': Image.name,
                #                     'image_file': Image.image_file})
                count += 1 
        print("IN THIS SECTION")
        return TemplateResponse(request,'admin/admin_template.html')
        



admin.site.register(Image, ImagesAdmin)