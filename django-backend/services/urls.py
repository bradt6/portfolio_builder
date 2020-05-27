from django.urls import path
from .views import ServiceAPIDetail, ServiceAPIList

urlpatterns = [
    path("service/", ServiceAPIList.as_view(), name="api-service-list"), 
    path("service/<str:slug>/", ServiceAPIDetail.as_view(), name="api-service-detail"),
]