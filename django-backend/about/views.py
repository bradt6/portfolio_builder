from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutPage
# Create your views here.
class AboutPageView(TemplateView):
    template_name = "about/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['about_data'] = AboutPage.objects.all()[0]
        context['about_data'] = AboutPage.objects.get(pk=1)
        context['name'] =AboutPage.objects.get(pk=1).name_of_bussiness

        return context