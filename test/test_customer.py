import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Busca en el directorio padre

from src.models.customer import Customer

def test_nombre_completo():
    cliente = Customer(1, "Stefanie", "Y", "Frye", 79, "97 Oak Avenue")
    assert cliente.full_name() == "Stefanie Y. Frye"
