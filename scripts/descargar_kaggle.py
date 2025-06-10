import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Ruta donde guardar el dataset
save_path = '/app/data/raw'
dataset_name = 'oktayrdeki/traffic-accidents'

# Verificar existencia del archivo de autenticación
kaggle_json_path = '/root/.kaggle/kaggle.json'
assert os.path.exists(kaggle_json_path), f"❌ No se encontró {kaggle_json_path}"

# Crear carpeta si no existe
os.makedirs(save_path, exist_ok=True)

# Inicializar y autenticar API
api = KaggleApi()
api.authenticate()

# Descargar y descomprimir
print(f"⬇️ Descargando dataset: {dataset_name}")
api.dataset_download_files(dataset_name, path=save_path, unzip=True)

print("✅ ¡Descarga completa! Archivos disponibles en:", save_path)

