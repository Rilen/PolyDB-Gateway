# 🚀 PolyDB Gateway

> **Camada de abstração e gateway unificado para acesso a múltiplos bancos de dados com observabilidade nativa.**

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-00000f?style=for-the-badge&logo=mysql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

---

## 📋 Visão Geral

O **PolyDB Gateway** é uma solução de infraestrutura leve desenvolvida para simplificar a interação entre aplicações e diversos ecossistemas de bancos de dados relacionais. Ele centraliza a gestão de conexões, padroniza as respostas em JSON e fornece uma camada de métricas pronta para monitoramento (Prometheus/Grafana).

### ✨ Diferenciais
- **Acesso Unificado:** Uma única API para consultar PostgreSQL, MySQL e SQLite.
- **Observabilidade:** Coleta distribuída de latência de query, erros e conexões ativas.
- **Interface Padronizada:** Respostas JSON consistentes, independente do dialeto SQL do banco de dados.
- **Pronto para Cloud:** Estrutura conteinerizada ideal para deploys em Cloud Run ou Kubernetes.

---

## 🔄 Rotina e Papel do Especialista de Dados

Neste projeto, o **Cientista/Engenheiro de Dados** atua como o arquiteto da informação. O seu trabalho rotineiro utilizando o PolyDB Gateway envolve:

1.  **Governança de Dados:** Definir no arquivo `databases.yaml` quais fontes de dados a empresa pode acessar com segurança.
2.  **Monitoramento de Performance:** Usar o **Grafana** para identificar queries lentas (gargalos) que podem estar afetando a produção.
3.  **Sanitização de Consultas:** Garantir que o Gateway esteja entregando JSONs limpos para que o **Programador** não precise tratar tipos de dados complexos de bancos antigos.
4.  **Escalabilidade:** Configurar novos clusters e conectá-los ao Gateway sem que a aplicação final precise mudar uma única linha de código.

---

## 🏗️ Arquitetura do Sistema

```mermaid
flowchart TD
    subgraph Admins ["Gestão de Infraestrutura"]
        DataRole[Engenheiro / Cientista / Analista de Dados]
    end

    subgraph Consumers ["Consumidores da API"]
        Devs[Programadores / Analistas de Sistemas]
        Apps[Aplicações / Microserviços]
    end

    subgraph Gateway ["PolyDB Gateway Instance"]
        API[FastAPI Gateway]
        Config[Configuração de Conexões]
        Auth[Camada de Autenticação]
        ConnMgr[Gerenciador de Conexões]
        Engine[Engine de Query JSON]
        Metrics[Coletor de Métricas]
    end

    subgraph Data ["Data Layer (Heterogênea)"]
        PG[(PostgreSQL)]
        MY[(MySQL)]
        SQ[(SQLite Local)]
    end

    subgraph Observability ["Stack de Observabilidade"]
        PR[Prometheus]
        GR[Grafana]
    end

    %% Fluxo de Gestão de Dados
    DataRole -- "Define Conexões (YAML)" --> Config
    DataRole -- "Monitora Performance" --> GR

    %% Fluxo de Consumo
    Devs -- "Consultas via JSON" --> API
    Apps -- "Requisições API" --> API
    
    %% Processamento Interno
    API --> Auth
    Auth --> ConnMgr
    ConnMgr --> Engine
    Engine --> PG
    Engine --> MY
    Engine --> SQ
    
    %% Fluxo de Métricas
    API --> Metrics
    Metrics --> PR
    PR --> GR
```

---

## 🚀 Como Iniciar (Demonstração Local)

### 1. Preparar o Ambiente
```powershell
# Clonar o repositório e entrar na pasta
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Subir Infraestrutura (Docker)
```powershell
# Inicia containers de Postgres, MySQL, Prometheus e Grafana
docker compose -f docker/docker-compose.yml up -d
```

### 3. Popular Ecossistema de Dados
```powershell
# Gera dados ricos em todos os bancos para apresentação
python scripts/seed_presentation.py
```

### 4. Executar o Gateway
```powershell
python api/gateway.py
```

### 5. Dashboards & API
- **API Docs (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Métricas Brutas (Prometheus):** [http://localhost:9090](http://localhost:9090)
- **Visualização (Grafana):** [http://localhost:3000](http://localhost:3000) (Login: admin/admin)

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.13+ com FastAPI.
- **Configuração:** YAML para gestão dinâmica de inventário de bancos.
- **Monitoramento:** Prometheus Client para exportação de métricas.
- **Infra:** Docker & Docker Compose para stack de bancos e monitoramento.

---

## 📄 Documentação Detalhada

Links para documentos de apoio e blueprint:
- [Arquitetura Completa](docs/architecture.md)
- [Fluxo de Requisição](docs/request-flow.md)
- [Resumo de Handover](docs/handover.md)

---

## 📌 Autor

**Rilen T. L.**  
*Data Engineering & API Architecture*  
📍 Rio das Ostras — RJ
