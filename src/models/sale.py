class Sale:
    def __init__(self, sale_id, employee_id, customer_id, product_id, quantity, discount, total_price, sale_time, transaction_number):
        self._sale_id = sale_id
        self._employee_id = employee_id
        self._customer_id = customer_id
        self._product_id = product_id
        self._quantity = quantity
        self._discount = discount
        self._total_price = total_price
        self._sale_time = sale_time
        self._transaction_number = transaction_number

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def product_id(self):
        return self._product_id

    @property
    def quantity(self):
        return self._quantity

    @property
    def discount(self):
        return self._discount

    @property
    def total_price(self):
        return self._total_price

    @property
    def sale_time(self):
        return self._sale_time

    @property
    def transaction_number(self):
        return self._transaction_number

