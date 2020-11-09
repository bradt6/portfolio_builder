from django.contrib import admin

from .models import Image

from django.contrib.admin import sites

from django.urls import path
from django.conf.urls import url

from django.shortcuts import render
from django.template.response import TemplateResponse

# from .views import AddManyImages 


    # path('upload-images/', addManyImages, name='upload-images'),
# class CustomAdminSite(admin.AdminSite):
#     def get_urls(self):
#         urls = super(CustomAdminSite, self).get_urls()
#         custom_urls = [
#             url('/admin/images/image/add/', addManyImages, name="upload-images")
#         ]
#         return urls + custom_urls

# @admin.register(Image, site=addManyImages)

# class ImagesAdmin(admin.ModelAdmin):
#     # add_view= 'images_templates/admin_template.html'
# #     # change_form_template = 'images_templates/admin_template.html'

#     def add_view(self, request):
#         print("Before")
#         if request.method == "POST":
#             print("HERE")
#             print("REQUEST:", request)
#             name = request.POST.get('name')
#             length = request.POST.get('length')
#             print("LENGTH :", length)

#             count = 0
#             for file_num in range(0, int(length)):
#                 Image.objects.create(
#                     name=f"{name}{count}",
#                     image_file=request.FILES.get(f"images{file_num}")
#                 )
#                 count += 1 
#         # return super().change_view(request,  'images_templates/admin_template.html')
#         return TemplateResponse(request, 'images_templates/admin_template.html')

# admin.site.register(Image, ImagesAdmin)

class ImagesAdmin(admin.ModelAdmin):
    # change_form_template = 'images_templates/admin_template.html'
    change_form_template = 'admin/admin_template.html'

    def get_urls(self):
        print("In the get URLS METHOD")
        urls = super().get_urls()
        custom_urls = [
            path('admin:upload-images/', self.admin_site.admin_view(self.addManyImages), name='upload-images'),
        ]
        print(custom_urls)
        return urls + custom_urls
    
    def addManyImages(self, request):
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
        # return TemplateResponse(request,'admin/admin_template.html')
        # return TemplateResponse(request,'images_templates/admin_template.html')
        return render(request, 'admin/admin_template.html')


admin.site.register(Image, ImagesAdmin)