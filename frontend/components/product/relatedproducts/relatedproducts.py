from django_components import Component, register

@register("relatedproducts")
class RelatedProducts(Component):
    template_file = 'relatedproducts.html'

    def get_related_products(self, current_product_id, related_products):
        # Filter out the current product and return up to 3 others
        return [p for p in related_products if p["id"] != current_product_id][:3]

    def get_context_data(self, related_products, *args, **kwargs):
        """Return context data for the template"""

        related_products = self.get_related_products(current_product_id=1, related_products=related_products)
        return {
            "size": kwargs.get("size", ""),
            "classes": kwargs.get("classes", ""),
            "related_products": related_products,
           }