

# Create your models here.
from django.db import models

class Product(models.Model):
    productname = models.CharField(max_length=200,)  # Name of the product
    image = models.ImageField(upload_to='products/')       # Image of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price with up to 2 decimal places
    details = models.TextField()                                  # Product details (description)
    
    # created_at = models.DateTimeField(auto_now_add=True)          # Timestamp for when the product was added
    # updated_at = models.DateTimeField(auto_now=True)              # Timestamp for when the product was updated

    def __str__(self):
        return self.productname


from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    productname = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    details = models.TextField()

    def __str___(self):
        return self.productname

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart of {self.user.username}"
    

class CartItem(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.productname}"

    
    def get_total_price(self):
        total = 0
        for cart_item in self.cartitem_set.all():
            total += cart_item.product.price * cart_item.quantity
        return total

