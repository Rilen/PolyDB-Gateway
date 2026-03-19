# System Architecture (v1.1)

```mermaid
flowchart LR

A[Client Applications] --> B[Directus API Layer]

B --> C[PostgreSQL]
B --> D[MySQL]

subgraph Observability
    E[Prometheus] --> C
    E --> D
    F[Grafana] --> E
end
```
