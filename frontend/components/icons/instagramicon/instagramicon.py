from django_components import Component, register

@register("instagramicon")
class InstagramIcon(Component):
    template_file = 'instagramicon.html'

    def get_context_data(self, *args, **kwargs):
        """Return context data for the template"""
        return {
            "size": kwargs.get("size", ""),
            "classes": kwargs.get("classes", ""),
        }