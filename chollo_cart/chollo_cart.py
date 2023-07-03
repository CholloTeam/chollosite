from decimal import Decimal
from django.conf import settings
from chollo_main.models import Product


class Cart:
    def __init__(self, request):
        """
        initialize the cart
        """
        self.session = request.session
        chollo_cart = self.session.get(settings.CART_SESSION_ID)
        if not chollo_cart:
            # save an empty chollo_cart in the session
            chollo_cart = self.session[settings.CART_SESSION_ID] = {}
        self.chollo_cart = chollo_cart

    def add(self, product, quantity=1, override=1, overide_quantity=False):
        """
        Add a product to the cart or update its quantity
        :param product:
        :param quantity:
        :param override:
        :param overide_quantity:
        :return:
        """
        product_id = str(product.id)
        if product_id not in self.chollo_cart:
            self.chollo_cart[product_id] = {'quantity': 0,
                                            'price': str(product.price)}
        if overide_quantity:
            self.chollo_cart[product_id]['quantity'] = quantity
        else:
            self.chollo_cart[product_id]['quantity'] += quantity

        self.save()
    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True


    def remove(self, product):
        """
        Remove a product from the cart.
        :param product:
        :return:
        """
        product_id = str(product.id)
        if product_id in self.chollo_cart:
            del self.chollo_cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        :return:
        """
        product_ids = self.chollo_cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        chollo_cart = self.chollo_cart.copy()
        for product in products:
            chollo_cart[str(product.id)]['product'] = product
        for item in chollo_cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        :return:
        """
        return sum(item['quantity'] for item in self.chollo_cart.values())

    def get_total_price(self):
        """
        Count all items in the cart.
        :return:
        """

        ##### CHECK ON THIS PLEASE!! ENSURE THERE"S A REASON WHY IT"S NOT DECIMAL

        return sum(Decimal(item['price']) * Decimal(item['quantity']) for item in self.chollo_cart.values())

    def clear(self):
        # Remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

