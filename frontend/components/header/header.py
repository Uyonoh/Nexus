from django.http import HttpRequest
from django_components import Component, register
from frontend.middleware.threadlocals import get_current_request
from cart.views import get_or_create_cart


@register('header')
class Header(Component):
    template_file = 'header.html'
   
    def get_context_data(self, *args, **kwargs):
        """Return context data for the template"""
        print(get_current_request())
        return {
            "cart": get_or_create_cart(get_current_request()),
        }