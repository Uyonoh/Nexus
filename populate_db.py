import random
from django.contrib.auth import get_user_model
from products.models import *
from orders.models import *
from inventory.models import *
from reviews.models import *
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image

User = get_user_model()

def create_sample_image(name="product"):
    img = Image.new('RGB', (300, 300), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    buf = BytesIO()
    img.save(buf, format='PNG')
    return ContentFile(buf.getvalue(), name=f"{name}.png")

# Create categories
category_names = ['Laptops', 'Desktops', 'System Components']
categories = [Category.objects.get_or_create(name=name)[0] for name in category_names]

# Create product types
product_types = ['Gaming', 'Workstation', 'Ultrabook', 'Budget', 'Enthusiast']
product_type_objs = [ProductType.objects.get_or_create(name=name)[0] for name in product_types]

# Create users
users = [User.objects.create_user(username=f'user{i}', email=f'user{i}@example.com', password='password123') for i in range(3)]

# Generate products
sample_specs = {
    "CPU": "Intel i7",
    "RAM": "16GB",
    "Storage": "512GB SSD",
    "GPU": "NVIDIA GTX 1660"
}

for cat in categories:
    for i in range(5):
        product = Product.objects.create(
            name=f"{cat.name[:-1]} Model {i+1}",
            description=f"A sample {cat.name[:-1].lower()} for testing.",
            category=cat,
            product_type=random.choice(product_type_objs),
            price=random.randint(500, 2000),
            original_price=random.randint(600, 2200),
            specs=sample_specs,
            rating=random.randint(1, 5),
            is_new=bool(random.getrandbits(1))
        )   
        for j in range(5):  
            image = create_sample_image(f"{cat.name}_{i+1}_image_{j+1}")
            ProductImage.objects.create(product=product, image=image, is_main=(j == 0))  # Mark the first image as main     
        Inventory.objects.create(product=product, quantity=random.randint(5, 50))    
        for _ in range(random.randint(1, 3)):
            Review.objects.create(
                user=random.choice(users),
                product=product,
                rating=random.randint(1, 5),
                title=f"Review for {product.name}",
                content="This is a sample review. Product works well!",
                helpful=random.randint(0, 10),
                verified=bool(random.getrandbits(1))
            )

# Create sample orders
for user in users:
    products = Product.objects.order_by('?')[:3]
    total = sum(p.price for p in products)
    order = Order.objects.create(user=user, total_amount=total, status=random.choice(['pending', 'completed', 'cancelled']))
    for product in products:
        OrderItem.objects.create(order=order, product=product, quantity=random.randint(1, 2), price=product.price)

print("✅ Sample data created.")
