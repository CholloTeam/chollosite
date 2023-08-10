from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from chollosite.chollo_cart.chollo_cart import Cart
from chollosite.chollo_cart.forms import CartAddProductForm
from chollosite.chollo_main.models import Product


# Create your views here.

@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        clean_data = form.cleaned_data
        cart.add(product=product,
                 quantity=clean_data['quantity'],
                 overide_quantity=clean_data['override'])
        return redirect('chollo_cart:cart_detail')


# Note the addition of 'id=' that was not formerly there
@require_POST
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('chollo_cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })
    return render(request, 'chollo_main/cart-details.html', {'cart': cart})

#
# @receiver(user_logged_in)
# def sync_cart_on_login(user, request):
#     cart = Cart(request.user)
#     for item in cart:
#         product = item['product']
#         quantity = item['quantity']
#         request.session['cart'][str(product.id)] = {
#             'quantity': quantity,
#             'price': str(product.price),
#         }
#
#
# @receiver(user_logged_out)
# def persist_cart_on_logout(user, request):
#     del request.session['cart']
