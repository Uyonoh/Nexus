from django import forms
from .models import Product, ProductImage, ProductSpec, ProductType, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ['slug', 'original_price', 'rating', 'is_new']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 rounded-md bg-indigo-900/30 text-white border border-indigo-700 focus:outline-none focus:ring-2 focus:ring-blue-400',
            })


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        # fields = '__all__'
        exclude = ['product', 'is_main', 'order']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 rounded-md bg-indigo-900/30 text-white border border-indigo-700 focus:outline-none focus:ring-2 focus:ring-blue-400',
            })

class ProductSpecForm(forms.ModelForm):
    class Meta:
        model = ProductSpec
        fields = '__all__'
        exclude = ['product']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 rounded-md bg-indigo-900/30 text-white border border-indigo-700 focus:outline-none focus:ring-2 focus:ring-blue-400',
            })