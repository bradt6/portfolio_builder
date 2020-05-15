from django.contrib import admin

from .models import Portfolio

# admin.site.register(Portfolio)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):

    list_display = ("name", "description", "images")
