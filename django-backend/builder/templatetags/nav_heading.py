from django import template
from builder.models import Builder, PageManager, Template
from about.models import AboutPage

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

@register.inclusion_tag('builder/nav.html')
def get_headings_inclusion_tags():
    pageManager_object = Builder.objects.values('pageManager')
    pageManager_id = pageManager_object[0]['pageManager']
    pageManager_name = PageManager.objects.get(id=pageManager_id)

    # aboutPage_object = AboutPage.objects.values('logo')
    # aboutPage_id = aboutPage_object[0].['id']
    # aboutPage_logo = AboutPage.objects.get(id=aboutPage_id)
    aboutPage_logo = AboutPage.objects.all()[0]
    # aboutPage_logo = AboutPage.objects.values('logo')[0]['logo']
    # aboutPage_logo = AboutPage.objects.get(id=aboutPage_id)

    heading_list = []
    
    if pageManager_name.services:
        heading_list.append(tuple(("services", "service-list")))
    if pageManager_name.portfolio:
        heading_list.append(tuple(("portfolio", "portfolio_list")))
    if pageManager_name.about:
        heading_list.append(tuple(("about", "about")))
    if pageManager_name.contact:
        heading_list.append(tuple(("contact", "contact")))

    return {'heading_list' : heading_list, 'aboutPage' : aboutPage_logo }
     