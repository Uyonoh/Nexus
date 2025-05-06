from django_components import Component, register

@register("imagegallery")
class ImageGallery(Component):
    template_file = 'imagegallery.html'

    def get_context_data(self, images, *args, **kwargs):
        """Return context data for the template"""
        return {
            "size": kwargs.get("size", ""),
            "classes": kwargs.get("classes", ""),
            "images": images,
        }