import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Busca en el directorio padre
from src.models.country import Country

def test_country_codigo_iso():
    country = Country(1, "Armenia", "AN")
    assert country.codigo_iso() == "AN"