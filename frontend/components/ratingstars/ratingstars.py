from django_components import Component, register

@register('ratingstars')
class RatingStars(Component):
    template_file = 'ratingstars.html'

    def get_context_data(self, rating, *args, **kwargs):
        """Return context data for the template"""
        # print(kwargs["product"])
        return {
            "classes": kwargs.get("classes", ""),
            "rating": rating,
        }