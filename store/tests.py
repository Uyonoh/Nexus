from django.test import TestCase
from django.urls import reverse
from store.models import Category, Product

class ProductListViewTest(TestCase):
    def test_product_list_view(self):
        # Create a category
        category = Category.objects.create(name='Test Category')

        # Create some products
        Product.objects.create(name='Test Product 1', description='Test Description 1', category=category, price=100, specs={})
        Product.objects.create(name='Test Product 2', description='Test Description 2', category=category, price=200, specs={})

        # Get the URL for the product list view
        url = reverse('product_list')

        # Get the response from the URL
        response = self.client.get(url)

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the template used is correct
        self.assertTemplateUsed(response, 'store/product_list.html')

        # Check that the products are passed to the template
        self.assertEqual(len(response.context['products']), 2)

class ProductDetailViewTest(TestCase):
    def test_product_detail_view(self):
        # Create a category
        category = Category.objects.create(name='Test Category')

        # Create a product
        product = Product.objects.create(name='Test Product', description='Test Description', category=category, price=100, specs={})

        # Get the URL for the product detail view
        url = reverse('product_detail', args=[product.pk])

        # Get the response from the URL
        response = self.client.get(url)

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the template used is correct
        self.assertTemplateUsed(response, 'store/product_detail.html')

        # Check that the product is passed to the template
        self.assertEqual(response.context['product'], product)
