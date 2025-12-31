"""
Lightweight version without image generation
Run with: python manage.py shell < populate_sample_data_simple.py
"""

import os
import sys
import random
from decimal import Decimal
from datetime import timedelta
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from django.utils import timezone
from faker import Faker

from products.models import Category, ProductType, Product, ProductSpec  # Change to your app name

fake = Faker()

def create_sample_data():
    """Create sample data without images"""
    print("Creating sample data...")
    
    # Clear existing data
    Category.objects.all().delete()
    ProductType.objects.all().delete()
    
    # Create product types
    product_types = []
    for name in ["Simple", "Configurable", "Digital", "Bundle"]:
        pt = ProductType.objects.create(
            name=f"{name} Product",
            slug=name.lower(),
            has_variants=(name in ["Configurable", "Bundle"]),
            digital_only=(name == "Digital")
        )
        product_types.append(pt)
    
    # Create categories
    laptops = Category.objects.create(name="laptops", slug="laptops")
    desktops = Category.objects.create(name="desktops", slug="desktops")
    components = Category.objects.create(name="components", slug="components")
    
    # Create subcategories
    # Category.objects.create(name="Smartphones", slug="smartphones", parent=laptops)
    # Category.objects.create(name="Laptops", slug="laptops", parent=laptops)
    Category.objects.create(name="gpus", slug="gpus", parent=components)
    # Category.objects.create(name="Women's Clothing", slug="womens-clothing", parent=desktops)
    # Category.objects.create(name="Furniture", slug="furniture", parent=components)
    # Category.objects.create(name="Kitchen", slug="kitchen", parent=components)
    
    # Sample products
    products_data = [
        {"name": "Premium Laptop", "price": 1299.99, "category": "laptops"},
        {"name": "Premium Desk", "price": 1599.99, "category": "desktops"},
        # {"name": "Smartphone Pro", "price": 899.99, "category": "smartphones"},
        {"name": "RTX-550", "price": 149.99, "category": "gpus"},
        {"name": "Fan", "price": 99.99, "category": "components"},
        {"name": "Cheap PC", "price": 179.99, "category": "desktops"},
    ]
    
    # Create products
    for data in products_data:
        category = Category.objects.get(slug=data["category"])
        
        product = Product.objects.create(
            name=data["name"],
            slug=data["name"].lower().replace(" ", "-"),
            description=fake.paragraph(nb_sentences=3),
            category=category,
            product_type=random.choice(product_types),
            price=Decimal(str(data["price"])),
            rating=random.randint(3, 5),
            created_at=timezone.now() - timedelta(days=random.randint(0, 14))
        )
        
        # Add some specifications
        specs = [
            {"key": "Brand", "value": fake.company()},
            {"key": "Color", "value": random.choice(["Black", "White", "Silver", "Blue"])},
            {"key": "Warranty", "value": random.choice(["1 Year", "2 Years"])},
        ]
        
        for spec in specs:
            ProductSpec.objects.create(
                product=product,
                key=spec["key"],
                value=spec["value"]
            )
    
    print(f"Created {Category.objects.count()} categories")
    print(f"Created {ProductType.objects.count()} product types")
    print(f"Created {Product.objects.count()} products")
    print(f"Created {ProductSpec.objects.count()} product specifications")
    print("\nSample data created successfully!")

if __name__ == "__main__":
    create_sample_data()