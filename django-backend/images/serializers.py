from rest_framework.serializers import ModelSerializer
from .models import Image

class ImageSerializer(ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"
       # extra_kwargs = {
       #     "url" : {
       #         "lookup_field": "slug",
       #         "view-name": "api-image-detail"
       #     }
       # }