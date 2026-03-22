# ==============================================================================
# 🐋 DOCKERFILE: POLYDB-GATEWAY (SRE ELITE EDITION)
# ==============================================================================
# Maintainer: Rilen T. L. - DataScience
# Base: Python 3.11-slim (Security Focused)
# ==============================================================================

FROM python:3.11-slim

LABEL Maintainer="Rilen T. L. - DataScience"
LABEL Project="PolyDB-Gateway"
LABEL Tier="Data Infrastructure"

# --- 1. RUNTIME CONFIG (Python optimization) ---
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# --- 2. SYSTEM DEPENDENCIES ---
# libpq-dev: Native PostgreSQL connectivity
# default-libmysqlclient-dev: Native MySQL connectivity (optimized)
# build-essential: Necessary for compiling some DS/ML packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    default-libmysqlclient-dev \
    pkg-config \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# --- 3. APPLICATION WORKDIR ---
WORKDIR /app

# --- 4. DEPENDENCY MANAGEMENT ---
COPY requirements.txt .

# PIP Optimization: --no-cache-dir and --upgrade pip
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# --- 5. SOURCE CODE & DATA HYGIENE ---
# O .dockerignore garante que SEG/, .git e logs não entrem na imagem
COPY scripts/ ./scripts/
COPY data/ ./data/

# --- 6. SECURITY: NON-ROOT USER (Best Practice) ---
RUN useradd -m polydb_user && \
    chown -R polydb_user:polydb_user /app
USER polydb_user

# --- 7. EXECUTION (Entrypoint focus) ---
# O container atua como um seeder/pipeline resiliente
CMD ["python", "scripts/seed_presentation.py"]
