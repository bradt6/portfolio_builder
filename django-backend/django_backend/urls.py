"""django_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from contacts import urls as contacts_url
# from images import urls as image_url
# from portfolio import urls as portfolio_url
# from services import urls as services_urls

from contacts import urls as contacts_url
from images import urls as image_url
from portfolio import urls as portfolio_url
from services import urls as services_urls
from about import urls as about_urls

from services.routers import urlpatterns as service_router_urls
from portfolio.routers import urlpatterns as portfolio_router_urls
from builder.routers import urlpatterns as builder_router_urls

# THIS IS NOT USED FOR PRODUCTION
from django.conf.urls.static import static
from django.conf import settings

from builder import urls as builder_url
# api_urls = contacts_url + image_url +  service_router_urls + portfolio_router_urls + portfolio_url
api_urls = service_router_urls + portfolio_router_urls + builder_router_urls

admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls)),
    path("", include(portfolio_url)),
    path("", include(builder_url)),
    path("", include(services_urls)),
    path("", include(about_urls)), 
    path("", include(contacts_url)), 
    path("", include(image_url)),
    
]

# THIS IS NOT USED FOR PRODUCTION
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT)

