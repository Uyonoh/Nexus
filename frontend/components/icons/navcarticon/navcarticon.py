from django_components import Component, register
import random

@register("navcarticon")
class NavCartIcon(Component):
    template_file = 'navcarticon.html'

    def get_context_data(self, cart, *args, **kwargs):
        """Return context data for the template"""
        return {
            "size": kwargs.get("size", ""),
            "classes": kwargs.get("classes", ""),
            "cart": cart,
        }