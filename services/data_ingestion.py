import pandas as pd
from src.database import DatabaseConnector
from factories.model_factory import ModelFactory 
from pydantic import ValidationError 
from typing import Dict, Any

class DataIngestionService:
    def __init__(self, db_conn: DatabaseConnector):
        self.db = db_conn

    def load_sales_from_csv(self, file_path: str) -> Dict[str, Any]:
        try:
            df = pd.read_csv(file_path)
            df.columns = [col.strip() for col in df.columns] 
        except FileNotFoundError:
            return {"status": "error", "message": f"Archivo no encontrado: {file_path}", "inserted_rows": 0, "attempted_rows": 0, "errors": []}
        except pd.errors.EmptyDataError:
            return {"status": "success", "message": "El archivo CSV está vacío.", "inserted_rows": 0, "attempted_rows": 0, "errors": []}
        except Exception as e: 
            return {"status": "error", "message": f"Error leyendo el archivo CSV: {str(e)}", "inserted_rows": 0, "attempted_rows": 0, "errors": []}

        # --- MAPEO DE NOMBRES DE COLUMNA ---
 
        column_mapping = {
            "SalesID": "sale_id",
            "SalesPersonID": "employee_id",
            "CustomerID": "customer_id",
            "ProductID": "product_id",
            "Quantity": "quantity",
            "Discount": "discount",
            "TotalPrice": "total_price",
            "SalesDate": "sale_time", 
            "TransactionNumber": "transaction_number",
        }


        sale_object = ModelFactory.create_sale(column_mapping) # Esto devuelve un objeto Sale

        sale_tuple_for_db = (
            sale_object.SalesID,
            sale_object.SalesPersonID,
            sale_object.ProductID,
            sale_object.Quantity,
            sale_object.Discount,
            sale_object.TotalPrice,
            sale_object.TransactionNumber,
            sale_object.SalesDate.strftime('%Y-%m-%d %H:%M:%S') if sale_object.SalesDate else None, # Formatear datetime
            sale_object.CustomerID,
            )

        query = """
        INSERT IGNORE INTO sales
        (sale_id, employee_id, product_id, quantity, discount, total_price, transaction_number, sale_time, customer_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
        """
        