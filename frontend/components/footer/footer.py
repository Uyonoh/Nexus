from django_components import Component, register

@register('footer')
class Footer(Component):
    template_file = 'footer.html'

    def get_context_data(self, *args, **kwargs):
        """Return context data for the template"""
        return {
            "classes": kwargs.get("classes", ""),
        }