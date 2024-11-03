

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import Product

class EcomTestCase(TestCase):

    # This method will run before every test, setting up necessary data.
    def setUp(self):
        # Create a sample product for testing
        self.product = Product.objects.create(
            Productname='Test Product',
            price=100.0,
            details='Test product description.'
        )
        # Set up the client for making HTTP requests
        self.client = Client()

    # Test URLs
    def test_urls(self):
        # Test the URL for the product list page
        response = self.client.get(reverse('ecom:product_list'))
        self.assertEqual(response.status_code, 200)

        # Test the URL for the product detail page with a valid product ID
        response = self.client.get(reverse('ecom:product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)

    # Test Views
    def test_product_list_view(self):
        # Check if the product list view works and uses the correct template
        response = self.client.get(reverse('ecom:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecom/product_list.html')
        self.assertContains(response, 'Test Product')  # Check if the product appears on the page

    def test_product_detail_view(self):
        # Check if the product detail view displays the product's details
        response = self.client.get(reverse('ecom:product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ecom/product_detail.html')
        self.assertContains(response, 'Test Product')  # Check for the product name
        self.assertContains(response, 'Test product description.')  # Check for product description

    # Test Models
    def test_product_model(self):
        # Test if the product model saves data correctly
        product = Product.objects.get(id=self.product.id)
        self.assertEqual(product.productname, 'Test Product')
        self.assertEqual(product.price, 100.0)
        self.assertEqual(product.details, 'Test product description.')

