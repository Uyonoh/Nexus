from django_components import Component, register

@register('header')
class Header(Component):
    template_file = 'header.html'