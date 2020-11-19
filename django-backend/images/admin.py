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
# from .views import AddManyImages 

from django.urls import reverse
from django.utils.safestring import mark_safe

# def upload_images():
#     url = reverse('image:upload-images')
#     return mark_safe(f'<a href="{url}">View</a>')



class ImagesAdmin(admin.ModelAdmin):
    change_form_template = "admin/admin_template.html"
    print("IN IMAGESADMIN")
    def get_urls(self):
        urls = super().get_urls()
        my_url = [path('upload_images/', self.admin_site.admin_view(self.addManyImages2))]
        new_urls = urls +my_url
        print(new_urls)
        return new_urls

    def addManyImages2(self, request):
        print("Before")
        if request.method == "POST":
            print("HERE")
            print("REQUEST:", request)
            name = request.POST.get('name')
            length = request.POST.get('length')
            print("LENGTH :", length)

            count = 0
            for file_num in range(0, int(length)):
                Image.objects.create(
                    name=f"{name}{count}",
                    image_file=request.FILES.get(f"images{file_num}")
                )
                count += 1 
        print("IN THIS SECTION")
        return TemplateResponse(request,'admin/admin_template.html')
        # return TemplateResponse(request,'images_templates/admin_template.html')
        # return render(request, 'admin/admin_template.html')
        # template = loader.get('admin/admin_template.html')
        # return HttpResponse(template.render(request, template))

# custom_admin = ImagesAdmin()
# custom_admin.register(Image)
# admin.site.register(Image, ImagesAdmin)
admin.site.register(Image, ImagesAdmin)

# site = ImagesAdmin()
# site.register(Image)
# site.register(Group, GroupAdmin)
# site.register(User, UserAdmin)
