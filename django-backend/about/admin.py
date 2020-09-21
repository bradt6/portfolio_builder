from django.contrib import admin
from .models import AboutPage, OpeningHours, SocialMediaAccount
# Register your models here.

@admin.register(AboutPage)
class AboutAdmin(admin.ModelAdmin):
    pass

@admin.register(OpeningHours)
class OpeningHoursAdmin(admin.ModelAdmin):
    pass

@admin.register(SocialMediaAccount)
class SocialMediaAccountAdmin(admin.ModelAdmin):
    pass

