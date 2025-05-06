from django_components import Component, register

@register("shieldcheckicon")
class ShieldCheckIcon(Component):
    template_file = 'shieldcheckicon.html'

    def get_context_data(self, *args, **kwargs):
        """Return context data for the template"""
        return {
            "size": kwargs.get("size", ""),
            "classes": kwargs.get("classes", ""),
        }