from rest_framework.reverse import reverse
from rest_framework.serializers import ModelSerializer

from .models import Builder, PageManager, Template


class TemplateSerializer(ModelSerializer):
    class Meta:
        model = Template
        fields = "__all__"
class PageManagerSerializer(ModelSerializer):
    class Meta:
        model = PageManager
        fields = "__all__"

class BuilderSerializer(ModelSerializer):
    page_manager = PageManagerSerializer(read_only=True)
    template_serializer = TemplateSerializer(read_only=True)
    class Meta:
        model = Builder
        fields = "__all__"