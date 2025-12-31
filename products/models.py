from django.db import models
from django.core.exceptions import ValidationError
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from datetime import timedelta
from django.utils import timezone
import itertools

class Category(MPTTModel):
    """Hierarchical product classification"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, 
                           null=True, blank=True, related_name='children')
    
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class ProductType(models.Model):
    """Product variant classification"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    has_variants = models.BooleanField(default=False)
    digital_only = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    
    category = models.ForeignKey(Category, related_name='products',
                                on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, related_name='products',
                                    on_delete=models.CASCADE)
    
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, 
                                       null=True, blank=True, db_index=True)
    rating = models.IntegerField(default=0, db_index=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    @property
    def is_new(self):
        now = timezone.now()
        created = self.created_at
        return (now - created) <= timedelta(days=7)
    
    @is_new.setter
    def is_new(self, value: bool):
        now = timezone.now()
        if not value:
            self.created_at = now - timedelta(days=7)
            self.save()
            return
        self.created_at = now
        self.save()
        return
        

    # Image handling
    @property
    def thumbnail(self):
        try:
            return self.images.filter(is_main=True).first().image.url
        except AttributeError:
            return '/static/images/default-product.png'

    @property
    def image_set(self):
        return self.images.all()

    # Review handling
    @property
    def reviews(self):
        return self.review_set.select_related('user').order_by('-date')

    def clean(self):
        if self.original_price and self.original_price < self.price:
            raise ValidationError(
                "Original price must be higher than current price"
            )
        
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            for i in itertools.count(1):
                if not Product.objects.filter(slug=slug).exists():
                    break
                slug = f"{base_slug}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ProductSpec(models.Model):
    """Structured product specifications"""
    product = models.ForeignKey(Product, related_name='specs',
                               on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ['product', 'key']

    def __str__(self):
        return f"{self.key}: {self.value}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images',
                               on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    is_main = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image for {self.product.name}"

    def save(self, *args, **kwargs):
        if self.is_main:
            # Ensure only one main image exists
            self.product.images.update(is_main=False)
        super().save(*args, **kwargs)
        # If product has no main image, set the first one as main
        if not self.product.images.filter(is_main=True).exists():
            main = self.product.images.all()[0]
            main.is_main = True
            main.save()