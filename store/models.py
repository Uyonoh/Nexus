from django.db import models
from django.conf import settings

class Category(models.Model):
    """ Product category """
    # TODO
    # Categories shold be plurals

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class ProductType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    specs = models.JSONField()
    # image = models.ImageField(upload_to='products/')
    rating = models.IntegerField(default=0)
    is_new = models.BooleanField(default=True)

    @property
    def image(self, i=0):
        return self._images.all()[i].image.url
    
    @property
    def images(self):
        return [self._images.all()[i].image.url for i in range(self._images.all().count())]
    
    @property
    def reviews(self):
        return [self.review_set.all()[i] for i in range(self.review.all().count())]
    

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    is_main = models.BooleanField(default=False)  # You can optionally mark one image as the "main" image

    def __str__(self):
        return f"Image for {self.product.name}"

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    helpful = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: {self.content}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name
