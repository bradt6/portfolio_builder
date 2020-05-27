from django.urls import path
from .views import PortfolioAPIDetail, PortfolioAPIList


urlpatterns = [
    path("portfolio/", PortfolioAPIList, name="api-portfolio-list"),
    path("portfolio/<str:slug>/", PortfolioAPIDetail.as_view(), name="api-portfolio-detail"),
]