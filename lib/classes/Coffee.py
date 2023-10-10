class Coffee():
    def __init__(self, name):
        self.name = name

        self._orders = []
        self._customer_list = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and len(name) > 2 and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("Name can only be set once and must be at least 3 characters.")

    def orders(self):
        return self._orders
    
    def customers(self):
        return list(set(self._customer_list))
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        sum = 0
        for order in self._orders:
            print(order)
            if isinstance(order.price, float):
                sum = sum + order.price
        avg = sum/len(self._orders)
        return avg


    def __repr__(self):
        return f"{self.name}"

