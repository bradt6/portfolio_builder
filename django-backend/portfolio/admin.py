from django.contrib import admin

from .models import Portfolio

from images.models import PortfolioImage 

class ImageInline(admin.TabularInline):
    model = PortfolioImage

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    # change_form_template = "admin/admin_portfolio_images.html"
    list_display = ("name", "description")

    inlines = [
        ImageInline,
    ]

    # def get_images_for_gallery(self):
    #     queryset = Image.objects.order_by('-created_at').values()[:20]
    #     return queryset


    # def add_view(self, request, form_url='', extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['your_custom_data'] = self.get_images_for_gallery
    #     return super().add_view(request, form_url, extra_context=extra_context)

