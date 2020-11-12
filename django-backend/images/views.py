from rest_framework.generics import (ListAPIView, RetrieveAPIView)

from .models import Image
from .serializers import ImageSerializer
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageFormUpload, FileFieldForm

from django.contrib.admin import AdminSite 
from django.views.decorators.cache import never_cache
from django.contrib.admin.views.decorators import staff_member_required
def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/images/detail.html',{"section": 'images', "image": image})

class ImageAPIDetail(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = "slug"

class ImageAPIList(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

# class AddManyImages(AdminSite):
@staff_member_required
def addManyImages(request):
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
    return render(request,'admin/admin_template.html')
        # return render(request,'images_templates/admin_template.html', {'image_form': form})