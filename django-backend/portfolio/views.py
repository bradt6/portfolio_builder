from rest_framework.generics import (ListAPIView, RetrieveAPIView)

from .models import Portfolio
from .serializers import PortfolioSerializer

class PortfolioAPIDetail(RetrieveAPIView):
    queryset = Portfolio.objects.all()
    serialzer_class = PortfolioSerializer
    lookup_field = "slug"

class PortfolioAPIList(ListAPIView):
    queryset = Portfolio.objects.all()
    serialzer_class = PortfolioSerializer