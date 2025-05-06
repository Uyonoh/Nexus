from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.
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
