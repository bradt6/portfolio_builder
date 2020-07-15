from django.urls import path
from .views import PortfolioAPIDetail, PortfolioAPIList, PortfolioList, PortfolioDetail


urlpatterns = [
#    path("portfolio/", PortfolioAPIList.as_view(), name="api-portfolio-list"),
#    path("portfolio/<str:slug>/", PortfolioAPIDetail.as_view(), name="api-portfolio-detail"),
    path("portfolio/", PortfolioList.as_view(), name="portfolio_list"),
    path("portfolio/<str:slug>/", PortfolioDetail.as_view(), name="portfolio_detail"),
]