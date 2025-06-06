class Customer:
    def __init__(self, customer_id, first_name, middle_initial, last_name, city_id, address):
        self._customer_id = customer_id
        self._first_name = first_name
        self._middle_initial = middle_initial
        self._last_name = last_name
        self._city_id = city_id
        self._address = address

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def first_name(self):
        return self._first_name

    @property
    def middle_initial(self):
        return self._middle_initial

    @property
    def last_name(self):
        return self._last_name

    @property
    def city_id(self):
        return self._city_id

    @property
    def address(self):
        return self._address

    def full_name(self):
        if self._middle_initial:
            return f"{self._first_name} {self._middle_initial}. {self._last_name}"
        return f"{self._first_name} {self._last_name}"