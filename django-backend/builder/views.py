from .models import Builder, PageManager, Template
from .serializers import BuilderSerializer, PageManagerSerializer, TemplateSerializer

from django.views.generic import TemplateView
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import get_object_or_404


class HomePageView(TemplateView):
    template_name = "builder/template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["builder"] = Builder.objects.all()

    #    This get the template object
        template_object = Builder.objects.values('template')
        template_id = template_object[0]['template']
        template_name = Template.objects.get(id=template_id)
        context["template"] = template_name

        # This get the pageManger object
        pageManager_object = Builder.objects.values('pageManager')
        pageManager_id = pageManager_object[0]['pageManager']
        pageManger_name = PageManager.objects.get(id=pageManager_id)
        context['pageManagerData'] = pageManger_name

        return context

class RetreiveAPIDetail(RetrieveAPIView):
    queryset = Builder.objects.all()
    serializer_class = BuilderSerializer