from django.urls import path
from .views import PortfolioAPIDetail, PortfolioAPIList, portfolioList


urlpatterns = [
#    path("portfolio/", PortfolioAPIList.as_view(), name="api-portfolio-list"),
    path("portfolio/<str:slug>/", PortfolioAPIDetail.as_view(), name="api-portfolio-detail"),
    path("portfolio/", portfolioList.as_view(), name="portfolio_list"),
]