import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from chollo_cart.forms import CartAddProductForm
from . models import Category, Product

# Create your views here.


def home(request):
    categories = list(Category.objects.all())

    # Select six random categories
    random_category = random.sample(categories, k=6)

    # Select random product from the categories
    random_products = []
    for category in random_category:
        # Retrieve a random product from each catogory
        random_product = Product.objects.filter(category=category).order_by('?').first()
        random_products.append(random_product)

    return render(request, "chollo_main/index.html",
                  {'random_products': random_products})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, "chollo_main/product_list.html",
                  {'category': category,
                  'categories': categories,
                  'products': products})


def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id,
                                slug=slug,
                                available=True
                                )
    cart_product_form = CartAddProductForm()
    return render(request,
                  "chollo_main/product.html",
                  {"product": product,
                   "cart_product_form": cart_product_form,
                   }
                  )


@login_required
def dashboard(request):
    return render(request, 'registration/login.html',
                  {'section': 'dashboard'})


def signin(request):
    return render(request, "chollo_main/signin.html")


def signup(request):
    return render(request, "chollo_main/signup.html")


def cart_details(request):
    return render(request, "chollo_main/cart-details.html")

