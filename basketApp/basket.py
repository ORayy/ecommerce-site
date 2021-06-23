


class Basket():
    """
    A base Basket class, providing some default behaviours that
    can be inherited or overridden, as necessary.
    """
    # initializing/creating a session for the User
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    # add to basket function
    def add(self, product, qty):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)

        # adding new data to the session
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': qty}

        self.session.modified = True

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())

