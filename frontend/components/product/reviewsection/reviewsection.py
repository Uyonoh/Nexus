from django_components import Component, register

@register("reviewsection")
class ReviewSection(Component):
    template_file = 'reviewsection.html'

    def get_context_data(self, product_id, reviews, *args, **kwargs):
        """Return context data for the template"""
        return {
            "size": kwargs.get("size", ""),
            "classes": kwargs.get("classes", ""),
            "product_id": product_id,
            "reviews": reviews,
        }