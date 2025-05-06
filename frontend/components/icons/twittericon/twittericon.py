from django_components import Component, register

@register("twittericon")
class TwitterIcon(Component):
    template_file = 'twittericon.html'

    def get_context_data(self, *args, **kwargs):
        """Return context data for the template"""
        return {
            "size": kwargs.get("size", ""),
            "classes": kwargs.get("classes", ""),
        }