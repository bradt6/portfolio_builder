from django.urls import path
from .views import ServiceAPIDetail, ServiceAPIList, ServiceListView, ServiceDetailView

urlpatterns = [
    # path("service/", ServiceAPIList.as_view(), name="api-service-list"), 
    # path("service/<str:slug>/", ServiceAPIDetail.as_view(), name="api-service-detail"),
    path("service/", ServiceListView.as_view(), name="service-list"),
    path("service/<str:slug>/", ServiceDetailView.as_view(), name="service-detail"),
    ]