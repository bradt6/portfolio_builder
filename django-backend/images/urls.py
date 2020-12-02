from django.urls import path
from .views import ImageAPIDetail, ImageAPIList, image_detail, addManyImages

urlpatterns = [
    path("image/", ImageAPIList.as_view(), name="api-image-list"),
    path("image/<str:slug>/", ImageAPIDetail.as_view(), name="api-image-detail"),
    path('detail/<int:id>/<slug:slug>/', image_detail, name='detail'),
    # path('upload-images-trial/', addManyImages, name='upload-images-trial'),
    # path('admin/image/upload-images', addManyImages, name="upload_images"),
    path('admin/images/image/add/upload-images/', addManyImages, name="upload_images"),
    path('upload-images/', addManyImages, name="upload_images"),
    path('admin/images/upload-images/', addManyImages, name="admin_upload_images"),
]