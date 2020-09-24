from django.urls import path
from .views import AboutPageView
from contacts.views import ContactForm

urlpatterns = [
#    path("portfolio/", PortfolioAPIList.as_view(), name="api-portfolio-list"),
#    path("portfolio/<str:slug>/", PortfolioAPIDetail.as_view(), name="api-portfolio-detail"),
    path("about/", AboutPageView.as_view(), name="about"),
    # path("contact/", ContactUsPage.as_view(), name="contact"),
    # path('contact_me/', ContactForm, name='contact_create'),
]