import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Busca en el directorio padre

from src.models.customer import Customer
from src.factories.model_factory import ModelFactory
from src.models.sale import Sale
from src.models.employee import Employee
from src.models.category import Category
from src.models.city import City
from src.models.country import Country
from datetime import datetime

def test_create_customer():
    """Verifica la correcta creación de un objeto Customer."""
    row_data = {"CustomerID": 1, "FirstName": "Natalia", "MiddleInitial": "A", "LastName": "Natalia", "CityID": 10, "Address": "123 Main St"}

    result = ModelFactory.create_customer(row_data)
    
    assert isinstance(result, Customer)
    assert result.customer_id==1
    assert result.first_name=="Natalia"
    assert result.middle_initial=="A"
    assert result.last_name=="Natalia"
    assert result.city_id==10
    assert result.address=="123 Main St"

def test_create_sale():
    """Verifica la correcta creación de un objeto Sale."""
    sale_date = datetime(2024, 5, 20)
    row_data = {
        "SalesID": 1001, "SalesPersonID": 5, "CustomerID": 1, "ProductID": 101,
        "Quantity": 2, "Discount": 0.1, "TotalPrice": 2160.90, "SalesDate": sale_date,
        "TransactionNumber": "TXN12345"
    }

    result = ModelFactory.create_sale(row_data)

    assert isinstance(result, Sale)
    assert result.employee_id == 5
    assert result.customer_id == 1
    assert result.product_id == 101
    assert result.quantity == 2
    assert result.discount == 0.1
    assert result.total_price == 2160.90
    assert result.sale_time == sale_date
    assert result.transaction_number == "TXN12345"

def test_create_employee():
    """Verifica la correcta creación de un objeto Employee."""
    birth_date = datetime(1990, 6, 15)
    hire_date = datetime(2020, 3, 1)
    row_data = {
        "EmployeeID": 5, "FirstName": "Jane", "MiddleInitial": "B", "LastName": "Smith",
        "BirthDate": birth_date, "Gender": "F", "CityID": 10, "HireDate": hire_date
    }

    result = ModelFactory.create_employee(row_data)

    assert isinstance(result, Employee)
    assert result.employee_id == 5
    assert result.first_name == "Jane"
    assert result.middle_initial == "B"
    assert result.last_name == "Smith"
    assert result.birth_date == birth_date
    assert result.gender == "F"
    assert result.city_id == 10
    assert result.hire_date == hire_date

def test_create_category():
    """Verifica la correcta creación de un objeto Category."""
    row_data = {"CategoryID": 1, "CategoryName": "Electronics"}
    
    result = ModelFactory.create_category(row_data)
    
    assert isinstance(result, Category)
    assert result.category_id == 1
    assert result.category_name == "Electronics"

def test_create_city():
    """Verifica la correcta creación de un objeto City."""
    row_data = {"CityID": 10, "CityName": "New York", "Zipcode": "10001", "CountryID": 1}

    result = ModelFactory.create_city(row_data)

    assert isinstance(result, City)
    assert result.city_id == 10
    assert result.city_name == "New York"
    assert result.zip_code == "10001"
    assert result.country_id == 1

def test_create_country():
    """Verifica la correcta creación de un objeto Country."""
    row_data = {"CountryID": 1, "CountryName": "United States", "CountryCode": "USA"}

    result = ModelFactory.create_country(row_data)

    assert isinstance(result, Country)
    assert result.country_id == 1
    assert result.country_name == "United States"
    assert result.country_code == "USA"