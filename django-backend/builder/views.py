from .models import Builder, PageManager, Template
from .serializers import BuilderSerializer, PageManagerSerializer, TemplateSerializer

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "builder/base.html"
