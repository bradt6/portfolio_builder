from django.forms import ModelForm, Form, FileField, ClearableFileInput
from .models import Image


class ImageFormUpload(ModelForm):
    class Meta:
        model = Image
        fields = ["name"]

class FileFieldForm(ImageFormUpload):
    images = FileField(widget=ClearableFileInput(attrs={'multiple': True}))

    class meta:
        fields = ImageFormUpload.Meta.fields + ['images',]
