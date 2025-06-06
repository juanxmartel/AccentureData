class SalesQueryBuilder:
    def __init__(self):
        self.query = "SELECT * FROM sales"
        self.filters = []
        self.params = {} # <-- Diccionario para guardar los parámetros de forma segura

    def with_customer(self, customer_id):
        self.filters.append("CustomerID = :customer_id")
        self.params['customer_id'] = customer_id
        return self

    def with_salesperson(self, salesperson_id):
        self.filters.append("SalesPersonID = :salesperson_id")
        self.params['salesperson_id'] = salesperson_id
        return self

    def with_min_quantity(self, quantity):
        self.filters.append("Quantity >= :min_quantity")
        self.params['min_quantity'] = quantity
        return self

    def with_date_range(self, start_date, end_date):
        self.filters.append("SalesDate BETWEEN :start_date AND :end_date")
        self.params['start_date'] = start_date
        self.params['end_date'] = end_date
        return self

    def build(self):
        query = self.query
        if self.filters:
            query += " WHERE " + " AND ".join(self.filters)
        return query, self.params 