import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.category import Category

def test_descripcion():
    categoria = Category(1, "Confections")
    assert categoria.descripcion() == "Categoría: Confections"
