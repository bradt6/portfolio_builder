from rest_framework.routers import SimpleRouter

from .viewsets import BuilderViewSet, PageViewSet, TemplateViewSet

api_router = SimpleRouter()
api_router.register("builder", BuilderViewSet, basename="api-builder")
api_router.register("pagemanager", PageViewSet, basename="api-pagemanager")
api_router.register("template", TemplateViewSet, basename="api-template")

# api_router.register("service", )

urlpatterns = api_router.urls
