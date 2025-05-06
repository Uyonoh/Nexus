from django_components import Component, register

@register('productcard')
class ProductCard(Component):
    template_file = 'productcard.html'

    def get_context_data(self, *args, **kwargs):
        """Return context data for the template"""
        # print(kwargs["product"])
        return {
            "product": kwargs.get("product", ""),
            "classes": kwargs.get("classes", ""),
        }