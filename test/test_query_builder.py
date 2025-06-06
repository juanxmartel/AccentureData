import pytest
from src.builder.sale_query_builder import SalesQueryBuilder 

@pytest.fixture
def builder():
    """Crea una nueva instancia del builder para cada test."""
    return SalesQueryBuilder()

def test_initial_state(builder):
    """Prueba que el builder se inicializa correctamente sin filtros."""
    query, params = builder.build()
    assert query == "SELECT * FROM sales"
    assert not params 

def test_with_customer_filter(builder):
    """Prueba el filtro por cliente."""
    query, params = builder.with_customer(123).build()
    assert "WHERE CustomerID = :customer_id" in query
    assert params["customer_id"] == 123

def test_with_min_quantity_filter(builder):
    """Prueba el filtro por cantidad mínima."""
    query, params = builder.with_min_quantity(10).build()
    assert "WHERE Quantity >= :min_quantity" in query
    assert params["min_quantity"] == 10

def test_chaining_multiple_filters(builder):
    """Prueba el encadenamiento de múltiples filtros."""
    query, params = builder.with_customer(456).with_min_quantity(5).build()
    assert "WHERE CustomerID = :customer_id AND Quantity >= :min_quantity" in query
    assert params["customer_id"] == 456
    assert params["min_quantity"] == 5

def test_no_filters_returns_base_query(builder):
    """Prueba que si no se añaden filtros, devuelve la consulta base."""
    query, params = builder.build()
    assert query == "SELECT * FROM sales"
    assert not params