import os
import django

import requests
from io import BytesIO
from PIL import Image
import random

from django.core.files.images import ImageFile
from faker import Faker
from django.core.files import File
from products.models import Category, ProductType, Product, ProductSpec, ProductImage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eccomerce.settings')
django.setup()

fake = Faker()

def download_image(width=800, height=600, tech_keywords=['computer', 'laptop', 'cpu', 'gpu']):
    """Download random tech-themed placeholder image"""
    try:
        keyword = random.choice(tech_keywords)
        url = f"https://source.unsplash.com/{width}x{height}/?{keyword}"
        response = requests.get(url, timeout=10)
        img = Image.open(BytesIO(response.content))
        img_io = BytesIO()
        img.save(img_io, format='JPEG')
        return ImageFile(img_io, name=f"{keyword}_{random.randint(1000,9999)}.jpg")
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

def create_product_images(product, num_images=3):
    """Create multiple images for a product"""
    try:
        # Create main image
        main_img = download_image(1200, 900, ['laptop', 'gaming', 'computer'])
        if main_img:
            ProductImage.objects.create(
                product=product,
                image=main_img,
                is_main=True,
                order=0
            )
        # Create additional images
        for i in range(1, num_images):
            img = download_image(800, 600, ['electronics', 'technology'])
            if img:
                ProductImage.objects.create(
                    product=product,
                    image=img,
                    is_main=False,
                    order=i
                )
    except Exception as e:
        print(f"Error creating images for {product}: {e}")

def create_categories():
    return {
        'Laptops': Category.objects.create(name='Laptops', slug='laptops'),
        'Desktops': Category.objects.create(name='Desktops', slug='desktops'),
        'Components': Category.objects.create(name='Components', slug='components')
    }

def create_product_types(categories):
    return {
        # Laptops
        'Gaming Laptops': ProductType.objects.create(
            name='Gaming Laptops',
            slug='gaming-laptops',
            has_variants=True,
            digital_only=False
        ),
        'Ultrabooks': ProductType.objects.create(
            name='Ultrabooks',
            slug='ultrabooks',
            has_variants=False,
            digital_only=False
        ),
        # Desktops
        'Gaming PCs': ProductType.objects.create(
            name='Gaming PCs',
            slug='gaming-pcs',
            has_variants=True,
            digital_only=False
        ),
        # Components
        'GPUs': ProductType.objects.create(
            name='Graphics Cards',
            slug='gpus',
            has_variants=True,
            digital_only=False
        ),
        'CPUs': ProductType.objects.create(
            name='Processors',
            slug='cpus',
            has_variants=True,
            digital_only=False
        )
    }

def create_laptop(product_type, category, specs_base):
    name = f"{fake.company()} {fake.random_element(['Predator', 'Nitro', 'Zenith', 'Vortex'])} {fake.random_int(3000, 9000)}"
    product = Product.objects.create(
        name=name,
        slug=name.lower().replace(' ', '-'),
        description=fake.paragraph(nb_sentences=10),
        category=category,
        product_type=product_type,
        price=fake.random_int(800, 3500),
        original_price=fake.random_int(900, 3700),
        rating=fake.random_int(3, 5),
        is_new=fake.boolean(chance_of_getting_true=70)
    )
    specs = {
        'Processor': f"{specs_base['cpu']} {fake.random_element(['i7', 'Ryzen 9', 'i9'])}",
        'RAM': f"{fake.random_element([16, 32, 64])}GB DDR{fake.random_element([4, 5])}",
        'Storage': f"{fake.random_element([512, 1000, 2000])}GB {fake.random_element(['SSD', 'NVMe SSD'])}",
        'Graphics': specs_base['gpu'],
        'Display': f"{fake.random_element([14, 15.6, 17.3])}\" {fake.random_element(['FHD', 'QHD', '4K'])} {fake.random_element(['144Hz', '240Hz', '60Hz'])}"
    } 
    for key, value in specs.items():
        ProductSpec.objects.create(product=product, key=key, value=value)
    create_product_images(product, num_images=random.randint(3, 5))
    return product

def create_gpu(product_type, category):
    model = fake.random_element([
        'RTX 4090', 'RX 7900 XTX', 'RTX 4080', 'RX 7800 XT'
    ])
    name = f"{fake.company()} {model}"
    product = Product.objects.create(
        name=name,
        slug=name.lower().replace(' ', '-'),
        description=fake.paragraph(nb_sentences=8),
        category=category,
        product_type=product_type,
        price=fake.random_int(500, 2000),
        original_price=fake.random_int(600, 2200),
        rating=fake.random_int(4, 5),
        is_new=fake.boolean(chance_of_getting_true=80)
    )
    specs = {
        'VRAM': f"{fake.random_element([12, 16, 24])}GB GDDR{fake.random_element([6, 6, 6, 6, 7])}X",
        'Clock Speed': f"{fake.random_int(1500, 2500)} MHz",
        'Memory Bus': f"{fake.random_element([192, 256, 384])}-bit",
        'Ports': fake.random_element([
            '3x DisplayPort 2.1, 1x HDMI 2.1',
            '2x DisplayPort 2.1, 2x HDMI 2.1'
        ])
    }
    for key, value in specs.items():
        ProductSpec.objects.create(product=product, key=key, value=value)
    create_product_images(product, num_images=random.randint(2, 4))
    return product

def generate_sample_data():
    print("Deleting old data...")
    Product.objects.all().delete()
    Category.objects.all().delete()
    ProductType.objects.all().delete()
    print("Creating categories...")
    categories = create_categories() 
    print("Creating product types...")
    product_types = create_product_types(categories)
    print("\nGenerating products:")
    # Generate Gaming Laptops
    print("- Gaming Laptops")
    for _ in range(8):
        create_laptop(
            product_types['Gaming Laptops'],
            categories['Laptops'],
            {'cpu': fake.random_element(['Intel', 'AMD']), 'gpu': 'RTX 4070'}
        )
    # Generate GPUs
    print("- Graphics Cards")
    for _ in range(6):
        create_gpu(product_types['GPUs'], categories['Components'])
    print("\nSample data generation complete!")

# if __name__ == '__main__':
generate_sample_data()

85266314