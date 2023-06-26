from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from chollo_cart.chollo_cart import Cart
from chollo_cart.forms import CartAddProductForm
from chollo_main.models import Product


# Create your views here.

@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        clean_data = form.cleaned_data
        cart.add(product=product,
                 quantity=clean_data['quantitiy'],
                 overide_quantity=clean_data['override'])
        return redirect('cart:cart_detail')


@require_POST
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })
    return render(request, 'chollo_main/cart-details.html', {'cart': cart})

