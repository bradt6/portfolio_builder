from django.urls import path
from .views import ContactAPIList, ContactAPIDetail, ContactListView

urlpatterns = [
    # path("contact/", ContactAPIList.as_view(), name="api-contact-list"),
    path("contact/<str:id>/", ContactAPIDetail.as_view(), name="api-contact-detail"),
    path("contact/", ContactListView.as_view(), name="contact_list"),
]