from django_components import Component, register

@register("listingsection")
class ListingSection(Component):
    template_file = 'listingsection.html'

    def get_context_data(self, *args, **kwargs):
        """Return context data for the template"""
        
        return {
            "category": kwargs.get("category", ""),
            "products": kwargs.get("products", ""),
            "classes": kwargs.get("classes", ""),
        }