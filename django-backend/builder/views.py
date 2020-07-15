from .models import Builder, PageManager, Template
from .serializers import BuilderSerializer, PageManagerSerializer, TemplateSerializer

from django.views.generic import TemplateView
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import get_object_or_404


class HomePageView(TemplateView):
    template_name = "builder/template.html"

    # model = Builder:w

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["builder"] = Builder.objects.all()
        # context["template"] = Builder.objects.values('template')
        template_id = Builder.objects.values('template')
        template_value = template_id[0]['template']
        template_name = Template.objects.get(id=template_value)
        context["template"] = template_value
        context["template_name"] = template_name.cdn_url_path
        # context['builder'] = Builder.objects.filter(pk=self.kwargs['id'])
        return context

# class HomePageView(TemplateView):
#     template_name = "builder/template.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["builder"] = Builder.objects.all()
#         builder_id = self.kwargs['builder']
#         builder = get_object_or_404(Builder, pk=builder_id)
#         context['builder'] = builder
#         return context

class RetreiveAPIDetail(RetrieveAPIView):
    queryset = Builder.objects.all()
    serializer_class = BuilderSerializer

# class indexView(IndexView):
#     template_name = "builder/template.html"