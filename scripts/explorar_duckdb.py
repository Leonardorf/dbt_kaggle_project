import duckdb
import pandas as pd

# Conectarse al archivo DuckDB
con = duckdb.connect("data/traffic.duckdb")

# Ver estructura de la tabla
print("Estructura de la tabla 'stg_accidents':\n")
print(con.execute("PRAGMA table_info('stg_accidents')").fetchdf())

# Ver algunas filas para inspeccionar nombres y formato
print("\nPrimeras filas de la tabla:\n")
print(con.execute("SELECT * FROM stg_accidents LIMIT 5").fetchdf())
