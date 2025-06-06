import pytest
import pandas as pd
from sqlalchemy import Engine
from src.database.db_connector import DatabaseConnector

@pytest.fixture(scope="module")
def db_connector():
    """
    Crea una instancia del DatabaseConnector que se reutilizará para todos los tests
    en este módulo. El scope="module" hace que se ejecute una sola vez.
    """
    try:
        connector = DatabaseConnector()
        return connector
    except Exception as e:
        pytest.fail(f"No se pudo conectar a la base de datos. Error: {e}")

def test_singleton_instance(db_connector):
    """
    Verifica que la clase DatabaseConnector siempre devuelve la misma instancia (patrón Singleton).
    """
    another_db_connector = DatabaseConnector()
    
    assert db_connector is another_db_connector, "DatabaseConnector no está implementando el patrón Singleton correctamente."

def test_connection_successful(db_connector):
    """
    Verifica que la conexión a la base de datos fue exitosa y se creó un engine.
    """
    engine = db_connector.get_engine()
    
    assert engine is not None, "El motor de la base de datos no debería ser Nulo."
    
    assert isinstance(engine, Engine), "El objeto retornado no es un motor de SQLAlchemy."

def test_run_query_returns_dataframe(db_connector):
    """
    Verifica que el método run_query ejecuta una consulta simple y devuelve un DataFrame.
    """
    query = "SELECT 1 AS test_col;"
    
    df = db_connector.run_query(query)
    
    # 1. Verificamos que el resultado es un DataFrame de Pandas
    assert isinstance(df, pd.DataFrame), "El método run_query debe devolver un DataFrame."
    
    # 2. Verificamos que el DataFrame no está vacío
    assert not df.empty, "El DataFrame resultante no debería estar vacío."
    
    # 3. Verificamos el contenido para estar 100% seguros
    assert df.shape == (1, 1), "El DataFrame debería tener una fila y una columna."
    assert df['test_col'][0] == 1, "El valor en la celda no es el esperado."