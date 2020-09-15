from django.contrib import admin
from .models import AboutPage
# Register your models here.

@admin.register(AboutPage)
class AboutAdmin(admin.ModelAdmin):
    pass