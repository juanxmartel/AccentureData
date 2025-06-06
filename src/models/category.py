class Category:
    def __init__(self, category_id, category_name):
        self._category_id = category_id
        self._category_name = category_name

    @property
    def category_id(self):
        return self._category_id

    @property
    def category_name(self):
        return self._category_name


