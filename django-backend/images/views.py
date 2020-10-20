from rest_framework.generics import (ListAPIView, RetrieveAPIView)

from .models import Image
from .serializers import ImageSerializer
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageFormUpload, FileFieldForm

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

def addManyImages(request):
    print("Before")
    if request.method == "POST":
        print("HERE")
        print("REQUEST:", request)
        # form = FileFieldForm(request.POST or None, request.FILES or None)
        # images = request.FILES.getlist('images')
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

        # if form.is_valid():
        #     i = 0
        #     for image in images:
        #         image_name = image.name
        #         print(image_name)
        #         image_name = str(i) 
        #         Image.objects.create(name=image_name, image_file=image)
        #         i = i +1
        # else:
        #     print("ERROR")
    # else:
    #     form = ImageFormUpload()

    return render(request,'images_templates/admin_template.html')
    # return render(request,'images_templates/admin_template.html', {'image_form': form})