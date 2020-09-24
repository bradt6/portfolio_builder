from rest_framework.generics import (ListAPIView, RetrieveAPIView)
from django.views.generic import ListView

from .models import Contact
from .serializers import ContactSerializer
from .forms import ContactForm
from django.http import HttpResponse
from django.shortcuts import render

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
    if request.method =='POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            new_contact = contact_form.save()
    else:
        contact_form = ContactForm()
    return render(request, 'contact_me/base.html',  {'contact_form': contact_form})
        

