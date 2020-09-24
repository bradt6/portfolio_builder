from rest_framework.generics import (ListAPIView, RetrieveAPIView)
from django.views.generic import ListView

from .models import Contact
from .serializers import ContactSerializer
from .forms import ContactForm
from django.http import HttpResponse
from django.shortcuts import render

from about.models import AboutPage

class ContactAPIDetail(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'id'

class ContactAPIList(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactListView(ListView):
    model = Contact
    template_name = "contact/list.html"

def contact_create(request):

    about_object = AboutPage.objects.get(pk=1)
    name = about_object.name_of_bussiness
    lat = about_object.lat
    lng = about_object.lng
    phone_number = about_object.phone_number
    opening_hours = about_object.opening_times
    social_accounts = about_object.social_accounts

    if request.method =='POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            new_contact = contact_form.save()
    else:
        contact_form = ContactForm()
    return render(request, 'contact_me/base.html',  {'contact_form': contact_form,
                                                    'name':name,
                                                    'lat':lat,
                                                    'lng':lng,
                                                    'phone_number': phone_number,
                                                    'opening_hours': opening_hours,
                                                    'social_accounts': social_accounts})
        

