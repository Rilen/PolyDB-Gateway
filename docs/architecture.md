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

style B fill:#1f77b4,color:#fff
style D fill:#2ca02c,color:#fff
style E fill:#ff7f0e,color:#fff
style L fill:#9467bd,color:#fff
