# Proyecto ETL con dbt y DuckDB: Análisis de Accidentes de Tránsito

Este proyecto realiza un pipeline de datos utilizando **Python**, **DuckDB**, y **dbt** para analizar datos abiertos sobre accidentes de tránsito. Los datos se descargan desde Kaggle y se procesan para generar modelos analíticos y reportes estructurados.

---

## 📁 Estructura del proyecto

```
dbt_kaggle_project/
├── data/                  # Base de datos y archivos CSV
│   ├── raw/               # Datos originales desde Kaggle
│   └── processed/         # (opcional) Datos transformados
│
├── docker/                # Dockerfile para el entorno dbt
├── kaggle_dbt/            # Proyecto dbt
│   ├── models/            # Modelos dbt
│   └── dbt_project.yml    # Configuración principal de dbt
│
├── scripts/               # Scripts auxiliares
│   ├── descargar_kaggle.py
│   ├── cargar_duckdb.py
│   └── explorar_duckdb.py
│
├── docker-compose.yml     # (opcional) Configuración de servicios
└── README.md              # Este archivo
```

---

## 🚀 ¿Cómo usar este proyecto?

1. **Clonar el repositorio** y posicionarse en la carpeta raíz:

   ```bash
   git clone https://github.com/tu-usuario/dbt_kaggle_project.git
   cd dbt_kaggle_project
   ```

2. **Instalar dependencias necesarias** (recomendado: entorno virtual):

   ```bash
   pip install -r requirements.txt
   ```

3. **Descargar el dataset de Kaggle**:

   Asegúrate de tener configuradas tus credenciales de Kaggle y ejecutá:

   ```bash
   python scripts/descargar_kaggle.py
   ```

4. **Cargar los datos en DuckDB**:

   ```bash
   python scripts/cargar_duckdb.py
   ```

5. **Ejecutar el proyecto dbt**:

   ```bash
   cd kaggle_dbt
   dbt run
   dbt show --select accidents_by_year
   ```

---

## 🌱 Mejoras futuras

- Crear un dashboard con **Streamlit** o **Dash**.
- Automatizar el pipeline con **Apache Airflow**.
- Añadir tests más avanzados en dbt.
- Conectar con herramientas de visualización como **Metabase** o **Superset**.
- Soporte para múltiples fuentes de datos.

---

## 👤 Autor

**Leonardo Villegas**  
Ingeniero en Sistemas, entusiasta de los datos abiertos y la ingeniería de datos.  
📧 [Contacto profesional en LinkedIn](www.linkedin.com/in/leonardo-r-f-villegas/)

---

## 📄 Licencia

Este proyecto se distribuye bajo la Licencia MIT.  
Ver el archivo [`LICENSE`](LICENSE) para más detalles.

