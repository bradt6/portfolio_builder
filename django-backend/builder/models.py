from django.db import models
import uuid

class Template(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    name = models.CharField(max_length=10)
    description = models.TextField(default="Cerulean")
    cdn_url_path = models.URLField(default="https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/cerulean/bootstrap.min.css")

class PageManager(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    about = models.BooleanField(default=False)
    portfolio = models.BooleanField(default=False)
    services = models.BooleanField(default=False)
    home = models.BooleanField(default=False)
    contact = models.BooleanField(default=False)

        # def get_absolute_url(self):
        # return reverse(
        #     "portfolio_detail", kwargs={"slug": self.slug}
        
    
class Builder(models.Model):
    # templateID = models.CharField(max_length=36)
    # pageMangerID = models.CharField(max_length=36)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)   
    template = models.OneToOneField(Template, on_delete=models.CASCADE)
    pageManager = models.OneToOneField(PageManager, on_delete=models.CASCADE)

    # class Meta:
    #     abstract = True

    def get_cdn(self):
        return self.template.cdn_url_path
    
    def get_default_template(self):
        return self.template


class HomePageModel(models.Model):
    banner = models.ImageField()
    #This should be short. get a quote. Email. Contact today. 
    call_to_action_text = models.CharField(max_length=27)
    short_description = models.TextField()

 # class ListCardComponent(models.Model):
     # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     # title = models.CharField(max_length = 64)
     # description = models.TextField()
     # style_cdn = models.URLField()

# class detailPageComponent(models.Model):

class BaseNavHeading(models.Model):
    isActive = models.BooleanField(default=False)
    icon = models.ImageField(default=None)

    class Meta:
        abstract = True

class about(BaseNavHeading):
    name = models.CharField(default = "about", editable=False, max_length=5)

class portfolio(BaseNavHeading):
    name = models.CharField(default = "portfolio", editable=False, max_length=10)

class service(BaseNavHeading):
    SERVICES = "services"
    SKILLS = "skills"
    NAME_CHOICES = [(SERVICES, "Services"),(SKILLS, "Skills")]
    name = models.CharField(choices= NAME_CHOICES,  default ="service", max_length=10)

class home(BaseNavHeading):
    name = models.CharField(default = "home", editable=False, max_length=5)

class contact(BaseNavHeading):
    name = models.CharField(default = "contact", editable=False, max_length=10)