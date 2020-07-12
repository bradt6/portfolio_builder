from .models import Builder, PageManager, Template
from .serializers import BuilderSerializer, PageManagerSerializer, TemplateSerializer

from django.views.generic import TemplateView
from rest_framework.generics import RetrieveAPIView

class HomePageView(TemplateView):
    template_name = "builder/template.html"

class RetreiveAPIDetail(RetrieveAPIView):
    queryset = Builder.objects.all()
    serializer_class = BuilderSerializer

