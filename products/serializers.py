from rest_framework import serializers
from .models import Category, ProductType, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    image = serializers.SerializerMethodField()  # Add a custom field for the image
    
    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, obj):
        # Return the image URL (it will use the `image` property you defined in the model)
        return obj.image  # Calls the `image` property method defined in Product