from rest_framework.serializers import ModelSerializer
from .models import Contact

class ContactSerializer(ModelSerializer):
    
    class Meta:
        model = ModelSerializer
        fields = "__all__"