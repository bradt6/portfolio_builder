from django.db import models
import uuid

class Template(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    name = models.CharField(max_length=10)
    description = models.TextField()
    cdn_url_path = models.URLField()

class PageManager(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    about = models.BooleanField()
    portfolio = models.BooleanField()
    services = models.BooleanField()
    home = models.BooleanField()
    contact = models.BooleanField()
class Builder(models.Model):
    # templateID = models.CharField(max_length=36)
    # pageMangerID = models.CharField(max_length=36)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)   
    template = models.OneToOneField(Template, on_delete=models.CASCADE)
    pageManager = models.OneToOneField(PageManager, on_delete=models.CASCADE)

    def get_cdn(self):
        return template.cdn_url_path



 # class ListCardComponent(models.Model):
     # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     # title = models.CharField(max_length = 64)
     # description = models.TextField()
     # style_cdn = models.URLField()

# class detailPageComponent(models.Model):
