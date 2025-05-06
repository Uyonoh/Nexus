from typing import List, Dict, Any

products: Dict[str, List[Dict[str, Any]]] = {
    "Featured Laptops": [
        {
            "id": 1,
            "name": "ProBook X7 Ultra",
            "description": '15.6" Gaming Laptop, RTX 4080, 32GB RAM, 2TB SSD',
            "price": 2499.99,
            "image": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
            "category": "laptops",
            "rating": 5,
            "isNew": True,
        },
        {
            "id": 2,
            "name": "ThinBook Air",
            "description": '13" Ultrabook, i7 12th Gen, 16GB RAM, 1TB SSD',
            "price": 1299.99,
            "originalPrice": 1499.99,
            "image": "https://images.unsplash.com/photo-1531297484001-80022131f5a1?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
            "category": "laptops",
            "rating": 4,
        },
        {
            "id": 3,
            "name": "WorkStation Pro",
            "description": '17" Professional Laptop, Xeon CPU, Quadro GPU, 64GB RAM',
            "price": 3199.99,
            "image": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
            "category": "laptops",
            "rating": 5,
        },
        {
            "id": 4,
            "name": "EcoBook 13",
            "description": '13" Eco-friendly Laptop, Ryzen 7, 16GB RAM, 512GB SSD',
            "price": 999.99,
            "image": "https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
            "category": "laptops",
            "rating": 4,
        },
    ],
    "High-perfoemance Desktops": [
        {
            "id": 5,
            "name": "Titan X Gaming Tower",
            "description": "i9-13900K, RTX 4090, 64GB DDR5, 4TB NVMe",
            "price": 3999.99,
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRr2D94zchYC6GTR86maf41bp0oqa4OgA58aw&s",
            "category": "desktops",
            "rating": 5,
            "isNew": True,
        },
        {
            "id": 6,
            "name": "Creator Workstation",
            "description": "Threadripper, RTX 3090, 128GB RAM, 8TB Storage",
            "price": 4599.99,
            "image": "https://images.unsplash.com/photo-1547082299-de196ea013d6?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
            "category": "desktops",
            "rating": 5,
        },
        {
            "id": 7,
            "name": "Mini Pro Cube",
            "description": "Compact Desktop, i7, RTX 3070, 32GB RAM",
            "price": 1799.99,
            "originalPrice": 1999.99,
            "image": "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
            "category": "desktops",
            "rating": 4,
        },
        {
            "id": 8,
            "name": "Office Elite Tower",
            "description": "Business Desktop, i5, 16GB RAM, 1TB SSD",
            "price": 899.99,
            "image": "https://images.unsplash.com/photo-1503252947848-7338d3f92f31?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
            "category": "desktops",
            "rating": 4,
        },
    ],
    "Premium Components": [
        {
            "id": 9,
            "name": "Quantum Z790 Motherboard",
            "description": "Premium Z790 motherboard with WiFi 6E and PCIe 5.0",
            "price": 399.99,
            "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
            "category": "components",
            "rating": 5,
            "isNew": True,
        },
        {
            "id": 10,
            "name": "Velocity RTX 4080 GPU",
            "description": "16GB GDDR6X, Ray Tracing, DLSS 3.0",
            "price": 1199.99,
            "image": "https://images.unsplash.com/photo-1591488320449-011701bb6704?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
            "category": "components",
            "rating": 5,
        },
        {
            "id": 11,
            "name": "HyperCool CPU Liquid Cooler",
            "description": "360mm RGB AIO Liquid CPU Cooler",
            "price": 189.99,
            "originalPrice": 219.99,
            "image": "https://images.unsplash.com/photo-1587202372616-b43abea06c2a?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
            "category": "components",
            "rating": 4,
        },
        {
            "id": 12,
            "name": "Thunder RAM 32GB Kit",
            "description": "DDR5-6000 RGB Memory (2x16GB)",
            "price": 229.99,
            "image": "https://images.unsplash.com/photo-1592664474505-51c549ad15c5?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
            "category": "components",
            "rating": 4,
        },
    ],
}


reviews: List[Dict[str, Any]] = [
    {
        "id": 1,
        "user": "Alex Thompson",
        "rating": 5,
        "date": "2023-11-15",
        "title": "Exceptional Performance",
        "content": "This laptop exceeds all expectations. The RTX 4080 handles everything I throw at it with ease. Build quality is top-notch and the screen is gorgeous.",
        "helpful": 24,
        "verified": True
    },
    {
        "id": 2,
        "user": "Sarah Chen",
        "rating": 4,
        "date": "2023-11-10",
        "title": "Great but runs hot",
        "content": "Amazing performance and beautiful display. Only downside is it can get quite warm during intensive gaming sessions.",
        "helpful": 18,
        "verified": True
    }
]

related_products: List[Dict[str, Any]] = [
    {
        "id": 2,
        "name": "ThinBook Air",
        "description": '13" Ultrabook, i7 12th Gen, 16GB RAM, 1TB SSD',
        "price": 1299.99,
        "originalPrice": 1499.99,
        "image": "https://images.unsplash.com/photo-1531297484001-80022131f5a1?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
        "category": "laptops",
        "rating": 4
    },
    {
        "id": 3,
        "name": "WorkStation Pro",
        "description": '17" Professional Laptop, Xeon CPU, Quadro GPU, 64GB RAM',
        "price": 3199.99,
        "image": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
        "category": "laptops",
        "rating": 5
    },
    {
        "id": 4,
        "name": "EcoBook 13",
        "description": '13" Eco-friendly Laptop, Ryzen 7, 16GB RAM, 512GB SSD',
        "price": 999.99,
        "image": "https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
        "category": "laptops",
        "rating": 4
    }
]

