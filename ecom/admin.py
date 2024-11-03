

# Register your models here.
from django.contrib import admin
from .models import Product


# Customize the Product Admin Panel
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'created_at', 'updated_at')  # Display these columns in the list view
    search_fields = ('product_name', 'details')  # Add search capability
    list_filter = ('created_at', 'updated_at')  # Add filters for easy navigation
    ordering = ('-created_at',)  # Default ordering of products by creation date (newest first)
    prepopulated_fields = {'slug': ('product_name',)}  # Prepopulate slug field if you have it in the model (optional)

# Register the Product model and custom admin panel


# ecom/admin.py
from django.contrib import admin
from .models import Product, Cart, CartItem  # Import your models

# Register your models once
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
