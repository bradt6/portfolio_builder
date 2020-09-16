from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutPage
# Create your views here.
class AboutPageView(TemplateView):
    template_name = "about/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['about_data'] = AboutPage.objects.all()[0]
        about_object = AboutPage.objects.get(pk=1)
        context['about_data'] = AboutPage.objects.get(pk=1)
        context['name'] = about_object.name_of_bussiness
        context['description'] = about_object.description
        context['opening_hours'] = about_object.opening_times 

        return context