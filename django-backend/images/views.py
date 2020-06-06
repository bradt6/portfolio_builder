from rest_framework.generics import (ListAPIView, RetrieveAPIView)

from .models import Image
from .serializers import ImageSerializer
class ImageAPIDetail(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = "slug"

class ImageAPIList(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer