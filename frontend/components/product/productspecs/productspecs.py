from django_components import Component, register
import re

@register("productspecs")
class ProductSpecs(Component):
    template_file = 'productspecs.html'

    def get_context_data(self, specs: dict, *args, **kwargs):
        """Return context data for the template"""

        formatted_specs = []
        # print(f"Specs: {specs}")
        # specs = {'Processor': 'AMD i9', 'RAM': '64GB DDR5', 'Storage': '512GB NVMe SSD', 'Graphics': 'RTX 4070', 'Display': '15.6" QHD 60Hz'}


        for key, value in specs.items():
            # Add a space before capital letters and capitalize the first word
            formatted_key = re.sub(r'(_)', r' \1', key).strip().capitalize()
            formatted_specs.append((formatted_key, value))

        return {
            "size": kwargs.get("size", ""),
            "classes": kwargs.get("classes", ""),
            "specs": formatted_specs,
        }