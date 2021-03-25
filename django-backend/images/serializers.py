from rest_framework.serializers import ModelSerializer
from .models import PortfolioImage

class ImageSerializer(ModelSerializer):

    class Meta:
        model = PortfolioImage
        fields = "__all__"
       # extra_kwargs = {
       #     "url" : {
       #         "lookup_field": "slug",
       #         "view-name": "api-PortfolioImage-detail"
       #     }
       # }