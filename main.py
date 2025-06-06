from src.database.db_connector import DatabaseConnector

db = DatabaseConnector()
df = db.run_query("SELECT * FROM sales LIMIT 5")
print(df.head())
