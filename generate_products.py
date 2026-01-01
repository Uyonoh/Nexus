import os, sys
import django

import requests
from io import BytesIO
from PIL import Image
import random
from dotenv import load_dotenv

load_dotenv()
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from django.core.files.images import ImageFile
from faker import Faker
from django.core.files import File
from products.models import Category, ProductType, Product, ProductSpec, ProductImage

fake = Faker()

def download_image(width=800, height=600, tech_keywords=['computer', 'laptop', 'cpu', 'gpu']):
    """Download random tech image using official Unsplash API"""
    ACCESS_KEY = os.environ['UNSPLASH_ACCESS_KEY']
    keyword = random.choice(tech_keywords)
    
    try:
        # Step 1: Get image metadata and a real hotlink URL
        api_url = f"https://api.unsplash.com/photos/random/?client_id={ACCESS_KEY}&query={keyword}"
        meta_data = requests.get(api_url).json()
        
        # Unsplash requires using their specific URL with width/height params
        image_url = f"{meta_data['urls']['raw']}&w={width}&h={height}&fit=crop"
        
        # Step 2: Download the actual image
        response = requests.get(image_url, timeout=10)
        img = Image.open(BytesIO(response.content))
        
        img_io = BytesIO()
        img.save(img_io, format='JPEG')
        return ImageFile(img_io, name=f"{keyword}_{random.randint(1000,9999)}.jpg")
    except Exception as e:
        print(f"Error: {e}")
        return None

def create_product_images(product: Product, num_images=3):
    """Create multiple images for a product"""
    try:
        # Create main image
        main_img = download_image(1200, 900, [product.category])
        if main_img:
            ProductImage.objects.create(
                product=product,
                image=main_img,
                is_main=True,
                order=0
            )
        # Create additional images
        for i in range(1, num_images):
            key = str(product.category)[:-1]
            if key == "Component": key = "Tech Component"
            img = download_image(800, 600, [key])
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
    name = f"""{fake.random_element(['HP', 'Shock', 'Dell', 'Asus'])} 
    {fake.random_element(['Predator', 'Nitro', 'Zenith', 'Vortex'])} 
    {fake.random_int(3000, 9000)}"""
    product = Product.objects.create(
        name=name,
        slug=name.lower().replace(' ', '-'),
        description=fake.paragraph(nb_sentences=10),
        category=category,
        product_type=product_type,
        price=fake.random_int(800, 3500),
        original_price=fake.random_int(900, 3700),
        rating=fake.random_int(3, 5),
    )
    product.is_new=fake.boolean(chance_of_getting_true=40) # Set after as it saves the instance
                                                           # which conflicts with creation
    specs = {
        'Processor': f"{specs_base['cpu']} {fake.random_element(['i7', 'Ryzen 9', 'i9'])}",
        'RAM': f"{fake.random_element([16, 32, 64])}GB DDR{fake.random_element([4, 5])}",
        'Storage': f"{fake.random_element([512, 1000, 2000])}GB {fake.random_element(['SSD', 'NVMe SSD'])}",
        'Graphics': specs_base['gpu'],
        'Display': f"{fake.random_element([14, 15.6, 17.3])}\" {fake.random_element(['FHD', 'QHD', '4K'])} {fake.random_element(['144Hz', '240Hz', '60Hz'])}"
    } 
    for key, value in specs.items():
        ProductSpec.objects.create(product=product, key=key, value=value)
    print(f"Creating Images for {name}...")
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
    )
    product.is_new=fake.boolean(chance_of_getting_true=40)
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
    print(f"Creating Images for {name}...")
    create_product_images(product, num_images=random.randint(2, 3))
    return product

def create_cpu(product_type, category):
    model = fake.random_element([
        'AMD Ryzen 7', 'AMD Ryzen 6', 'Intel Core i7', 'Intel Core i9'
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
    )
    product.is_new=fake.boolean(chance_of_getting_true=40)
    specs = {
        'Cores': f"{fake.random_element([2, 4, 8, 16])}",
        'Clock Speed': f"{fake.random_int(2500, 4500)} MHz",
    }
    if "Intel" in model:
        specs["Generation"] = fake.random_int(5, 13)
    for key, value in specs.items():
        ProductSpec.objects.create(product=product, key=key, value=value)
    print(f"Creating Images for {name}...")
    create_product_images(product, num_images=2)
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
    for _ in range(3):
        create_laptop(
            product_types['Gaming Laptops'],
            categories['Laptops'],
            {'cpu': fake.random_element(['Intel', 'AMD']), 'gpu': 'RTX 4070'}
        )
    # Generate Gaming PCs
    print("- Gaming PCs")
    for _ in range(2):
        create_laptop(
            product_types['Gaming PCs'],
            categories['Desktops'],
            {'cpu': fake.random_element(['Intel', 'AMD']), 'gpu': 'RTX 5090'}
        )
    
    # categories = {
    #     'Laptops': Category.objects.get(name='Laptops'),
    #     'Desktops': Category.objects.get(name='Desktops'),
    #     'Components': Category.objects.get(name='Components')
    # }
    
    # product_types = {
    #     # Laptops
    #     'Gaming Laptops': ProductType.objects.get(
    #         name='Gaming Laptops',
    #     ),
    #     'Ultrabooks': ProductType.objects.get(
    #         name='Ultrabooks',
    #     ),
    #     # Desktops
    #     'Gaming PCs': ProductType.objects.get(
    #         name='Gaming PCs',
    #     ),
    #     # Components
    #     'GPUs': ProductType.objects.get(
    #         name='Graphics Cards',
    #     ),
    #     'CPUs': ProductType.objects.get(
    #         name='Processors',
    #     )
    # }
    
    # Generate GPUs
    print("- Graphics Cards")
    for _ in range(2):
        create_gpu(product_types['GPUs'], categories['Components'])
    # Generate CPUs
    print("- CPU")
    for _ in range(2):
        create_cpu(product_types['CPUs'], categories['Components'])
    print("\nSample data generation complete!")

# if __name__ == '__main__':
generate_sample_data()

85266314