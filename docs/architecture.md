# System Architecture

```mermaid
flowchart LR

A[Client Applications] --> B[PolyDB Gateway API]

B --> C[Auth Layer]
B --> D[Connection Manager]
B --> E[Query Engine]

D --> F[(MySQL Cluster)]
D --> G[(PostgreSQL Cluster)]
D --> H[(SQLite / Local DB)]

E --> I[Query Validator]
E --> J[Execution Engine]
E --> K[JSON Response Formatter]

B --> L[Metrics Collector]

L --> M[Prometheus]
M --> N[Grafana Dashboard]
