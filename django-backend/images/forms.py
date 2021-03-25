from django.forms import ModelForm, Form, FileField, ClearableFileInput
from .models import PortfolioImage


class ImageFormUpload(ModelForm):
    class Meta:
        model = PortfolioImage
        fields = ["name"]

class FileFieldForm(ImageFormUpload):
    images = FileField(widget=ClearableFileInput(attrs={'multiple': True}))

    class meta:
        fields = ImageFormUpload.Meta.fields + ['images',]
