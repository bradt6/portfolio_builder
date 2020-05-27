from rest_framework.generics import (ListAPIView, RetrieveAPIView)

from .models import Service
from .serializers import ServiceSerializer

class ServiceAPIDetail(RetrieveAPIView):
    queryset = Service.objects.all()
    serialzer_class = ServiceSerializer
    lookup_field = "slug"

class ServiceAPIList(ListAPIView):
    queryset = Service.objects.all()
    serialzer_class =  ServiceSerializer
