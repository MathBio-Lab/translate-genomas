FROM python:3.11-slim AS builder

WORKDIR /app

# Evita que Python genere archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala las dependencias de Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --prefix=/install -r requirements.txt

# 🧩 Etapa 2: runtime (ligero y optimizado)
FROM python:3.11-slim

WORKDIR /app

# Copia dependencias desde la etapa anterior
COPY --from=builder /install /usr/local

# Copia el código de la aplicación
COPY . .

# Puerto para Uvicorn
EXPOSE 8000

# Variable de entorno para diferenciar entornos
ENV ENVIRONMENT=production

# Comando por defecto (usa múltiples workers con Uvicorn)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
