from rest_framework.generics import (ListAPIView, RetrieveAPIView)

from .models import Image
from .serializers import ImageSerializer
from django.shortcuts import get_object_or_404, render

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

