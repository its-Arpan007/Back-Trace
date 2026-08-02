# Database & Storage Architecture

This directory documents the PostgreSQL schema, SQLAlchemy ORM models, and Alembic migration strategies for BACKTRACE.

## Database Guidelines
- PostgreSQL 16 managed via `asyncpg`
- UUIDv4 primary keys for all entities
- Audit timestamps (`created_at`, `updated_at`)
- Alembic async migration workflow
