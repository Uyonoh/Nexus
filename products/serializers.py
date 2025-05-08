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
    category = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()  # Add a custom field for the image
    media = serializers.SerializerMethodField()
    specifications = serializers.SerializerMethodField()  # Add a custom field for the 
    is_new = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = '__all__'

    def get_category(self, obj):
        # Return the category name (it will use the `name` property you 
        return obj.category.name  # Calls the `name` property method 

    def get_image(self, obj):
        # Return the image URL (it will use the `image` property you defined in the model)
        return obj.thumbnail  # Calls the `image` property method defined in Product
    
    def get_media(self, obj):
        # Return the list of image URLs (it will use the `images` property you defined in the model)
        return [image.image.url for image in obj.image_set]
    
    def get_specifications(self, obj):
        # Return the list of specs (it will use the `specs` property you defined in the model)
        return dict([[spec.key, spec.value] for spec in obj.specs.all()])
    
    def get_is_new(self, obj):
        # Return the is_new value (it will use the `is_new` property you defined in the model)
        return obj.is_new