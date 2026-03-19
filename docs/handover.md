📄 PolyDB Platform — Blueprint / Handover Summary (Simplified v1.1)

1. Project Overview

PolyDB is a unified data management platform using Directus Headless CMS to provide instant REST/GraphQL APIs and a visual administrative interface for multiple databases.

Primary goals:
- Eliminate redundant API wrappers (FastAPI removal)
- Direct connection between Directus and Frontend
- Automated API generation (REST/GraphQL)
- RBAC (Role Based Access Control) out of the box

2. System Architecture

The system utilizes Directus as the core engine for data management and API delivery.

High-level architecture:
Clients
   ↓
Directus API (REST/GraphQL)
   ↓
Internal Engine (Directus)
   ↓
Target Databases (PostgreSQL / MySQL)

3. Repository Structure

poly-db-platform
│
├── README.md
│
├── docs
│   ├── architecture.md
│   └── handover.md
│
├── docker
│   └── docker-compose.yml
│
└── scripts
    └── seed_presentation.py

4. Configuration

Directus is configured via environment variables in `docker/docker-compose.yml`. Databases are connected as "External Collections" or the primary database of the instance.

5. Deployment Strategy

The entire stack is containerized with Docker, facilitating deployment on any cloud provider or VPS.

Client Apps
     ↓
Directus Engine
     ↓
Databases

6. Handover Notes

Project status:
- FastAPI Gateway removed for simplification
- Directus configured as primary API layer
- Seeding scripts updated for direct DB connection

Next steps:
- Configure all external databases in Directus interface
- Map roles/permissions for frontend applications
- Integrate frontend using Directus SDK

📌 Autor
Rilen T. L.
Platform Architecture
2026
