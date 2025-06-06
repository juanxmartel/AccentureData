class Employee:
    def __init__(self, employee_id, first_name, middle_initial, last_name, birth_date, gender, city_id, hire_date):
        self._employee_id = employee_id
        self._first_name = first_name
        self._middle_initial = middle_initial
        self._last_name = last_name
        self._birth_date = birth_date
        self._gender = gender
        self._city_id = city_id
        self._hire_date = hire_date

    @property
    def employee_id(self):
        return self._employee_id

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
    def birth_date(self):
        return self._birth_date

    @property
    def gender(self):
        return self._gender

    @property
    def city_id(self):
        return self._city_id

    @property
    def hire_date(self):
        return self._hire_date

