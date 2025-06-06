class Product:
    def __init__(self, product_id, product_name, price, category_id, class_type, modify_time, resistant, is_allergic, vitality_days):
        self._product_id = product_id
        self._product_name = product_name
        self._price = price
        self._category_id = category_id
        self._class_type = class_type
        self._modify_time = modify_time
        self._resistant = resistant
        self._is_allergic = is_allergic
        self._vitality_days = vitality_days

    @property
    def product_id(self):
        return self._product_id

    @property
    def product_name(self):
        return self._product_name

    @property
    def price(self):
        return self._price

    @property
    def category_id(self):
        return self._category_id

    @property
    def class_type(self):
        return self._class_type

    @property
    def modify_time(self):
        return self._modify_time

    @property
    def resistant(self):
        return self._resistant

    @property
    def is_allergic(self):
        return self._is_allergic

    @property
    def vitality_days(self):
        return self._vitality_days

