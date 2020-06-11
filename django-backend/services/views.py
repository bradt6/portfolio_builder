from rest_framework.generics import (ListAPIView, RetrieveAPIView, ListCreateAPIView)
# from django.contrib.auth.models import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    RedirectView,
    UpdateView
)

from .models import Service
from .serializers import ServiceSerializer

class ServiceAPIDetail(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "slug"

# This was changed for the create method. Still trying to get the view working with the viewset
# and router
class ServiceAPIList(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class =  ServiceSerializer
