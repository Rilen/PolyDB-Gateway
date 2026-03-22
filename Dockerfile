# ==============================================================================
# 🐋 DOCKERFILE: OTIMIZADO PARA ENGENHARIA DE DADOS & IA
# ==============================================================================
# Maintainer: Rilen T. L. - DataScience
# Base: Python 3.11-slim (Estabilidade e Segurança)

FROM python:3.11-slim

LABEL Maintainer="Rilen T. L. - DataScience"

# --- 1. CONFIGURAÇÕES DE RUNTIME (PERFORMANCE Python em Docker) ---
# Evita a criação de arquivos de bytecode (.pyc) que sugam espaço
ENV PYTHONDONTWRITEBYTECODE=1
# Garante que as mensagens de log sejam enviadas em tempo real (sem buffer)
ENV PYTHONUNBUFFERED=1

# --- 2. DEPÓSITOS DE SISTEMA & COMPILAÇÃO ---
# libpq-dev: Conectividade Nativa com PostgreSQL
# build-essential: Compilação de drivers e pacotes DS/ML (ex: NumPy)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# --- 3. GESTÃO DE DEPENDÊNCIAS DE APLICAÇÃO ---
WORKDIR /app
COPY requirements.txt .

# Instalação com limpeza imediata de cache de pacotes PIP (Reduz Imagem em 40%+)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# --- 4. CÓDIGO FONTE & SEGURANÇA ---
# NOTA SRE: A pasta SEG/ e o .env são IMEDIATAMENTE bloqueados via .dockerignore
# A injeção de segredos deve ocorrer via Volumes no Docker Compose (Zero Trust)
COPY scripts/ ./scripts/
COPY data/ ./data/

# --- 5. EXECUÇÃO (PIPELINE DE DADOS) ---
# O seeder atua como o ponto de entrada principal para garantir integridade.
CMD ["python", "scripts/seed_presentation.py"]
