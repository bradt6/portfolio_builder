from django.contrib import admin

from .models import Portfolio

from images.models import Image
# admin.site.register(Portfolio)

# class ImageInline(admin.TabularInline):
#     model = Image

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "get_images")
    # inlines = [
    #     ImageInline,
    # ]
