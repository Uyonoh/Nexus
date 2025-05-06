from django_components import Component, register

@register('herosection')
class HeroSection(Component):
    template_file = 'herosection.html'