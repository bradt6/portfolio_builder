from rest_framework.routers import SimpleRouter

from .viewsets import PortfolioViewSet

portfolio_router = SimpleRouter()
portfolio_router.register("portfolio", PortfolioViewSet, basename="api-portfolio")

urlpatterns = portfolio_router.urls