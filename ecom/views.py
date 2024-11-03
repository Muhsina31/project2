from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# View for adding a new product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the list of products after successful save
    else:
        form = ProductForm()
    
    return render(request, 'ecom/add_product.html', {'form': form})

# View for editing an existing product
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'ecom/edit_product.html', {'form': form, 'product': product})


# View for listing products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecom/product_list.html', {'products': products})

# View for displaying product details
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'ecom/product_detail.html', {'product': product})


#   View for Registration

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')  # Redirect to product list after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# view for home

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')




from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def create_product(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'create_product.html')

@login_required
def edit_product(request, product_id):
    # Logic to edit a product
    return render(request, 'edit_product.html')

@login_required
def delete_product(request, product_id):
    # Logic to delete a product
    return redirect('product_list')



from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Cart, CartItem
from ecom.models import Cart, CartItem, Product  # Import all relevant models


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.cartitem_set.all()  # Get all CartItems associated with this cart
    return render(request, 'cart_detail.html', {'cart': cart, 'items': items})




# Create your views here.

# @cache_page(60*1)
# def index(request):
    # car={"make":2001,"model":"maruti","num":[1,2,3,4]}

    # return render(request,"index.html",car)
# @cache_page(100*1)
# def product_list(request):
    # products=Product.objects.all()
    # return render(request,'product_list.html',{'products':products})



# def page1(request):
    # return render(request,"page1.html")

    
# Caching the Product List View:


from django.views.decorators.cache import cache_page
from django.shortcuts import render
from .models import Product

@cache_page(60 * 1)  # Cache for 1 minutes
def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecom/product_list.html', {'products': products})



# Using Low-Level Caching for Product Details

from django.core.cache import cache
from .models import Product

def product_detail(request, product_id):
    cache_key = f'product_{product_id}'
    product = cache.get(cache_key)
    
    if not product:
        product = Product.objects.get(id=product_id)
        cache.set(cache_key, product, timeout=60 * 15)
    
    return render(request, 'ecom/product_detail.html', {'product': product})
