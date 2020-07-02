from rest_framework.generics import (ListAPIView, RetrieveAPIView)

from .models import Portfolio
from .serializers import PortfolioSerializer

from django.views.generic import (ListView, DetailView)
class PortfolioAPIDetail(RetrieveAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    lookup_field = "slug"

class PortfolioAPIList(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioList(ListView):
    model = Portfolio
    template_name = "portfolio/list.html"

class PortfolioDetail(DetailView):
    queryset = Portfolio.objects.all()
    template_name = "portfolio/detail.html"