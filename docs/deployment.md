## Deployment Architecture

```mermaid
flowchart TB

subgraph Clients
A[Web Applications]
B[Mobile Apps]
C[Internal Systems]
end

subgraph API Layer
D[PolyDB Gateway API]
E[Auth Service]
end

subgraph Core Services
F[Connection Pool Manager]
G[Query Execution Engine]
H[Response Formatter]
end

subgraph Databases
I[(MySQL Cluster)]
J[(PostgreSQL Cluster)]
K[(SQLite / Local DB)]
end

subgraph Observability
L[Metrics Collector]
M[Prometheus]
N[Grafana Dashboard]
end

A --> D
B --> D
C --> D

D --> E
D --> F

F --> G
G --> H

G --> I
G --> J
G --> K

D --> L
L --> M
M --> N
