from src.models.customer import Customer
from src.models.product import Product
from src.models.sale import Sale
from src.models.employee import Employee
from src.models.category import Category
from src.models.city import City
from src.models.country import Country

class ModelFactory:

    @staticmethod
    def create_customer(row):
        return Customer(
            customer_id=row["CustomerID"],
            first_name=row["FirstName"],
            middle_initial=row["MiddleInitial"],
            last_name=row["LastName"],
            city_id=row["CityID"],
            address=row["Address"]
        )

    @staticmethod
    def create_product(row):
        return Product(
            product_id=row["ProductID"],
            product_name=row["ProductName"],
            price=row["Price"],
            category_id=row["CategoryID"],
            class_type=row["Class"],
            modify_time=row["ModifyDate"],
            resistant=row["Resistant"],
            is_allergic=row["IsAllergic"],
            vitality_days=row["VitalityDays"]
        )

    @staticmethod
    def create_sale(row):
        return Sale(
            sale_id=row["SalesID"],
            employee_id=row["SalesPersonID"],
            customer_id=row["CustomerID"],
            product_id=row["ProductID"],
            quantity=row["Quantity"],
            discount=row["Discount"],
            total_price=row["TotalPrice"],
            sale_time=row["SalesDate"],
            transaction_number=row["TransactionNumber"]
        )

    @staticmethod
    def create_employee(row):
        return Employee(
            employee_id=row["EmployeeID"],
            first_name=row["FirstName"],
            middle_initial=row["MiddleInitial"],
            last_name=row["LastName"],
            birth_date=row["BirthDate"],
            gender=row["Gender"],
            city_id=row["CityID"],
            hire_date=row["HireDate"]
        )

    @staticmethod
    def create_category(row):
        return Category(
            category_id=row["CategoryID"],
            category_name=row["CategoryName"]
        )

    @staticmethod
    def create_city(row):
        return City(
            city_id=row["CityID"],
            city_name=row["CityName"],
            zip_code=row["Zipcode"],
            country_id=row["CountryID"]
        )

    @staticmethod
    def create_country(row):
        return Country(
            country_id=row["CountryID"],
            country_name=row["CountryName"],
            country_code=row["CountryCode"]
        )
