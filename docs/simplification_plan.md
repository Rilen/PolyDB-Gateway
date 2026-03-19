# Implementation Plan: System Simplification (Removing FastAPI Gateway)

The objective is to remove the redundant FastAPI gateway and transition to a direct connection between Directus (Headless CMS) and the frontend.

## Proposed Changes

### 1. Code Cleanup
- [x] Remove `api/` directory (contains `gateway.py`).
- [x] Remove `config/databases.yaml` (gateway configuration).
- [ ] Simplify `requirements.txt` to only include dependencies for data seeding scripts.
- [ ] Remove `prometheus.yml` from root (if it's only for the gateway).

### 2. Documentation Updates
- [ ] Update `README.md` to reflect the simplified Directus-only architecture.
- [ ] Update `docs/architecture.md` to show the direct Directus connection.
- [ ] Update `docs/request-flow.md` to show Directus handling requests.
- [ ] Update `docs/handover.md` to reflect the new direction.

### 3. Docker Configuration
- [ ] Verify `docker/docker-compose.yml` provides a complete setup for its simplified role.
- [ ] Ensure Directus is the entry point for data management and API.

## Verification
- [ ] Ensure `docker compose` still starts correctly.
- [ ] Validate that seeding scripts still work against the databases.
- [ ] Confirm no broken links or outdated instructions in the documentation.
