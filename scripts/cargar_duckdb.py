import duckdb
import os

# Ruta del archivo CSV
csv_path = '/app/data/raw/Traffic_Accidents.csv'
assert os.path.exists(csv_path), f"❌ No se encontró el archivo {csv_path}"

# Ruta de la base de datos DuckDB
db_path = '/app/data/traffic.duckdb'

# Conectamos (creará el archivo si no existe)
con = duckdb.connect(database=db_path)

# Cargar CSV como tabla
con.execute("""
    CREATE OR REPLACE TABLE stg_accidents AS
    SELECT * FROM read_csv_auto('/app/data/raw/Traffic_Accidents.csv', HEADER=TRUE)
""")

# Verificamos filas
n_rows = con.execute("SELECT COUNT(*) FROM stg_accidents").fetchone()[0]
print(f"✅ Tabla 'stg_accidents' creada con {n_rows} filas")
