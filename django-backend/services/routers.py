from django.urls import path
from rest_framework.routers import SimpleRouter

from .viewsets import ServiceViewSet

api_router = SimpleRouter()
api_router.register("service", ServiceViewSet, basename='api-service')

urlpatterns = api_router.urls