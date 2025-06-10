# Dockerfile
FROM python:3.11-slim

# Evita prompts durante instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    unzip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Crea directorios de trabajo
WORKDIR /app

# Copia los archivos de requirements (se crean más adelante)
COPY requirements.txt .

# Instala dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el proyecto completo (excepto lo ignorado por .dockerignore)
COPY . .

# Comando por defecto
CMD [ "bash" ]
