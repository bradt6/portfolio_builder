from rest_framework.viewsets import ModelViewSet

from .models import Builder, Template, PageManager
from .serializers import BuilderSerializer, TemplateSerializer, PageManagerSerializer

class TemplateViewSet(ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

class PageViewSet(ModelViewSet):
    queryset = PageManager.objects.all()
    serializer_class = PageManagerSerializer

class BuilderViewSet(ModelViewSet):
    queryset = Builder.objects.all()
    serializer_class = BuilderSerializer

