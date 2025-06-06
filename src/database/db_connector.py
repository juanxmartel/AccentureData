from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from config import DATABASE_URL

class DatabaseConnector:
    _instance = None
    _engine = None
    _Session = None

    def __new__(cls):
        if cls._instance is None:
            print("Creando nueva instancia de DatabaseConnector...")
            cls._instance = super().__new__(cls)
            try:
                # Inicializamos el motor y la sesión en la CLASE
                cls._engine = create_engine(DATABASE_URL, echo=False)
                cls._Session = scoped_session(
                    sessionmaker(bind=cls._engine)
                )
            except Exception as e:
                print(f"Error al conectar a la base de datos: {e}")
                raise RuntimeError(f"Error al conectar a la base de datos: {str(e)}")
        return cls._instance

    def get_engine(self):
        """Retorna el motor de SQLAlchemy."""
        return self._engine

    def get_session(self):
        """Obtiene una nueva sesión de la base de datos."""
        if self._Session:
            return self._Session()
        else:
            print("Error: no está inicializada.")
            return None

    def run_query(self, query: str, params: dict = None) -> pd.DataFrame:
        """
        Ejecuta una consulta SQL (opcionalmente parametrizada) y devuelve los resultados.
        """
        session = self.get_session()
        if session is None:
            return pd.DataFrame()

        try:
            result = session.execute(text(query), params) 
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
            return df
        except SQLAlchemyError as e:
            print(f"Error al ejecutar la consulta: {e}")
            return pd.DataFrame()
        finally:
            session.close()
