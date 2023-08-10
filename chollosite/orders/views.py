from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from chollosite.chollo_cart.chollo_cart import Cart
from .tasks import order_created

# Create your views here.


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity']
                                         )
            # clear the cart
            cart.clear()

            # launch asynchronous task
            order_created.delay(order.id)

            return render(request,
                          'chollo_main/created.html',
                          {'order': order}
                          )
    else:
        form = OrderCreateForm()
    return render(request,
                  'chollo_main/create.html',
                  {'cart': cart, 'form': form}
                  )

