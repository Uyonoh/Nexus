from django_components import Component, register

@register("youtubeicon")
class YouTubeIcon(Component):
    template_file = 'youtubeicon.html'

    def get_context_data(self, *args, **kwargs):
        """Return context data for the template"""
        return {
            "size": kwargs.get("size", ""),
            "classes": kwargs.get("classes", ""),
        }