from django import template
from builder.models import Builder, PageManager, Template

register = template.Library()

@register.simple_tag
def get_theme():
    template_object = Builder.objects.values('template')
    template_id = template_object = template_object[0]['template']
    template_name = Template.objects.get(id = template_id)
    return template_name.cdn_url_path

@register.simple_tag
def get_headings():
    pageManager_object = Builder.objects.values('pageManager')
    pageManager_id = pageManager_object[0]['pageManager']
    pageManager_name = PageManager.objects.get(id=pageManager_id)
    return pageManager_name
    