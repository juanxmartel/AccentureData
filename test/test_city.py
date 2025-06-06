import sys 
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Busca en el directorio padre

from src.models.city import City

def test_city_ubicacion():
    city = City(1, "Armenia", "an", 1)
    assert city.ubicacion() == "Armenia (an)"