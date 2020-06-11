from rest_framework.viewsets import ModelViewSet

from .models import Portfolio
from .serializers import PortfolioSerializer

class PortfolioViewSet(ModelViewSet):
    lookup_field = "slug"
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer