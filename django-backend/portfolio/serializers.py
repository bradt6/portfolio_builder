from rest_framework.serializers import ModelSerializer
from .models import Portfolio
from images.serializers import ImageSerializer

class PortfolioSerializer(ModelSerializer):

    image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = "__all__"