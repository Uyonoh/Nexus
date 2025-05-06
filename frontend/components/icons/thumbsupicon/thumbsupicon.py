from django_components import Component, register

@register("thumbsupicon")
class ThumbsUpIcon(Component):
    template_file = 'thumbsupicon.html'

    def get_context_data(self, *args, **kwargs):
        """Return context data for the template"""
        return {
            "size": kwargs.get("size", ""),
            "classes": kwargs.get("classes", ""),
        }