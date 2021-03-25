from django.contrib import admin

from .models import PortfolioImage

from django.contrib.admin import sites

from django.urls import path
from django.conf.urls import url 

from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin #and these
from django.http import HttpResponse
from .views import addManyImages 

from django.urls import reverse
from django.utils.safestring import mark_safe

from django.forms import ModelForm

from django.http.response import JsonResponse
from django.http import HttpResponseRedirect


# def upload_images():
#     url = reverse('PortfolioImage:upload-images')
#     return mark_safe(f'<a href="{url}">View</a>')

class ImageAdminForm(ModelForm):
    class Meta:
        model = PortfolioImage
        fields = ["name"]


class ImagesAdmin(admin.ModelAdmin):
    change_form_template = "admin/admin_template.html"
    # add_form_template = "admin/admin_template.html"
    # form = ImageAdminForm
    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['your_custom_data'] = self.add_images_via_json(request)
        return super().add_view(request, form_url, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        my_url = [path('many1/', self.admin_site.admin_view(self.add_images_via_json)),
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
                PortfolioImage.objects.create(
                    name=f"{name}_{count}",
                    image_file=request.FILES.get(f"images{file_num}")
                )
                # return JsonResponse({'name': PortfolioImage.name,
                #                     'image_file': PortfolioImage.image_file})
                count += 1 
            print("IN THIS SECTION")
        # return TemplateResponse(request,'admin/admin_template.html')
            return HttpResponseRedirect(request.path_info)  
        return render(request, 'admin/admin_template.html')
        



    def add_images_via_json(self, request):
        print("entering Method via json return add images with a dictionary")
        
        if request.method == 'POST':
            name = request.POST.get('name')
            length = request.POST.get('length')
            print(f"Request name: {name}, Request.length: {length}")

            count = 0
            json_dict = {}
            for file_num in range(0, int(length)):
                image_name=f"{name}_{count}"
                image_file = request.FILES.get(f"images{file_num}")
                
                image_object = PortfolioImage()
                image_object.name = image_name 
                image_object.image_file = image_file
                image_object.save()

                # json_data.append(JsonResponse({'image_name': image_object.name}))
                json_dict[image_object.id] = {"image_name" : image_object.name}
                count += 1

            print("BEFORE METHOD")
            print("Length of json dictionary: ", len(json_dict))
            print(json_dict)
            if len(json_dict) > 0:
                print("IN METHOD")
                print("This is the json data array: ", json_dict)
                print("********** COMPLETE JSON COMPONENT **********")
                return JsonResponse(json_dict)
                # return JsonResponse({'data_array':json_data})
            else:
                return JsonResponse({'error' : 'the data wasnt loaded correctly'})

                
            



admin.site.register(PortfolioImage, ImagesAdmin)