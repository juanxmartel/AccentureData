class City:
    def __init__(self, city_id, city_name, zip_code, country_id):
        self._city_id = city_id
        self._city_name = city_name
        self._zip_code = zip_code
        self._country_id = country_id

    @property
    def city_id(self):
        return self._city_id

    @property
    def city_name(self):
        return self._city_name

    @property
    def zip_code(self): 
        return self._zip_code

    @property
    def country_id(self):
        return self._country_id
