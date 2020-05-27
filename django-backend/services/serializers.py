from rest_framework.serializers import ModelSerializer
from .models import Service
from images.serializers import ImageSerializer

class ServiceSerializer(ModelSerializer):
    image = ImageSerializer()
    
    class Meta:
        model = Service
        fields = "__all__"