from rest_framework.generics import (ListAPIView, RetrieveAPIView)

from .models import Contact
from .serializers import ContactSerializer

class ContactAPIDetail(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'id'

class ContactAPIList(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer