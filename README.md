# PolyDB Gateway

![Python](https://img.shields.io/badge/python-backend-blue)
![PostgreSQL](https://img.shields.io/badge/postgres-database-blue)
![MySQL](https://img.shields.io/badge/mysql-database-orange)
![API](https://img.shields.io/badge/API-gateway-green)

PolyDB Gateway is an API layer designed to provide unified access to multiple databases while offering monitoring, connection management and standardized JSON responses.

## Features

- Multi-database support (MySQL, PostgreSQL, SQLite)
- Connection pool manager
- Query execution engine
- JSON formatted responses
- Metrics and observability

## Architecture

```mermaid
flowchart LR

A[Client Applications] --> B[PolyDB Gateway API]

B --> C[Auth Layer]
B --> D[Connection Manager]
B --> E[Query Engine]

D --> F[(MySQL Cluster)]
D --> G[(PostgreSQL Cluster)]
D --> H[(SQLite)]

E --> I[Query Validator]
E --> J[Execution Engine]
E --> K[JSON Formatter]

B --> L[Metrics Collector]

L --> M[Prometheus]
M --> N[Grafana]

## Documentation

- Architecture: docs/architecture.md
- Request Flow: docs/request-flow.md
- Presentation: docs/presentation.md
