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

    # def get_dyanmic_info(self):
    #     pass
    # def add_view(self, request, form_url="admin/admin_template.html", extra_context=None):
    #     return super(ImagesAdmin, self).add_view(request, form_url="admin/admin_template.html", extra_context=None)

    print("IN IMAGESADMIN")
    def get_urls(self):
        urls = super().get_urls()
        my_url = [path('many1/', self.admin_site.admin_view(self.addManyImages2)),
                  path('many2/', addManyImages),]
        new_urls = my_url + urls
        print(new_urls)
        return new_urls

    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['osm_data'] = self.get_dynamic_info()
    #     return super(ImagesAdmin, self).change_view(
    #     request, object_id, form_url, extra_context=extra_context,
    # )

    # def get_form(self, request, obj=None, **kwargs):
    #     if request.user.is_superuser:
    #         kwargs['form'] = ImageAdminForm
    #     return super().get_form(request, obj, **kwargs)

    # def change_view(self, request, object_id, form_url = 'admin/admin_template.html', extra_context=None):
    #     extra_context = extra_context or {}
    #     if request.method == "POST":
    #         print("HERE")
    #         print("REQUEST:", request)
    #         name = request.POST.get('name')
    #         length = request.POST.get('length')
    #         print("LENGTH :", length)

    #         count = 0
    #         for file_num in range(0, int(length)):
    #             Image.objects.create(
    #                 name=f"{name}{count}",
    #                 image_file=request.FILES.get(f"images{file_num}")
    #             )
    #             count += 1 
    #     print("IN THIS SECTION")
    #     return super().change_view(request, object_id, form_url, extra_context=extra_context)

    def my_view(self, request):
        
    # ...
        context = dict(
            # Include common variables for rendering the admin template.
        self.admin_site.each_context(request),
        # Anything else you want in the context...
        key=value,
    )
        return TemplateResponse(request, 'admin/admin_template.html', context)  



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
