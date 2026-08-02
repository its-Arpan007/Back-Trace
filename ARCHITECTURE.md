# ARCHITECTURE.md - BACKTRACE Architectural Blueprint

## 1. System Vision & Paradigm

**BACKTRACE** is designed from first principles as an **AI-Powered Learning Intelligence Platform**. Unlike conversational chatbots or naive question banks, BACKTRACE treats student responses as diagnostic signals.

The architecture is built to support high-throughput, low-latency graph traversals, real-time diagnostic reasoning, mastery state tracking, and adaptive recommendations while preserving strict separation of concerns, testability, and maintainability.

---

## 2. Clean Architecture Principles

BACKTRACE enforces Clean Architecture across both Frontend and Backend environments:

```
                  +-----------------------------------+
                  |          Presentation             |
                  |   (Views, Controllers, Schemas)   |
                  +-----------------+-----------------+
                                    |
                                    v
                  +-----------------+-----------------+
                  |          Domain / Services        |
                  |    (Use Cases, Business Rules)    |
                  +-----------------+-----------------+
                                    |
                                    v
                  +-----------------+-----------------+
                  |       Data / Infrastructure       |
                  | (Repositories, DB, Network, Redis)|
                  +-----------------------------------+
```

### Key Rules:
1. **Source Code Dependencies Point Inward**: Business logic does not depend on DB drivers or HTTP frameworks.
2. **Repository Pattern**: All database interactions pass through abstract interfaces (`BaseRepository`), shielding services from ORM specifics.
3. **Immutability & Strongly-Typed DTOs**: Pydantic models in Python and Freezed DTOs in Dart guarantee data contract integrity at compile-time and runtime.
4. **Dependency Injection**: Dependencies are wired centrally (FastAPI `Depends()` on backend, Riverpod `Provider` on frontend).

---

## 3. Backend Architectural Layers

```
backend/app/
├── api/          --> Endpoints & HTTP Routing (FastAPI)
├── core/         --> Platform Config, Security, Exception Handlers, Logging
├── database/     --> Async SQLAlchemy Engine, Base Metadata, Session Providers
├── models/       --> DB Declarative Models & UUID/Timestamp Mixins
├── schemas/      --> Pydantic Validation & API Envelope DTOs
├── services/     --> Business Logic Execution & Redis Cache Management
├── repositories/ --> Async Database CRUD Operations (BaseRepository)
└── middlewares/  --> Global Tracing (Request ID) & Structured HTTP Logging
```

### Data Flow Example (Request Lifecycle):
1. **HTTP Request** arrives at FastAPI Endpoint in `app/api/v1/endpoints/`.
2. **Middleware** attaches unique `X-Request-ID` and logs request timing.
3. **Endpoint Layer** validates request payload against Pydantic schema in `app/schemas/`.
4. **Service Layer** (`app/services/`) executes domain logic, utilizing Redis for hot caching.
5. **Repository Layer** (`app/repositories/`) issues async SQL queries via SQLAlchemy 2.0 to PostgreSQL.
6. **API Response Envelope** (`BaseResponse[T]`) formats standardized JSON output.

---

## 4. Frontend Architectural Layers

```
frontend/lib/
├── core/         --> Config (EnvConfig), Network (Dio), Errors, DI (Riverpod)
├── theme/        --> AppTheme, HSL Colors, Typography (Outfit/Inter)
├── routes/       --> Navigation (GoRouter) & Path Registry
├── shared/       --> Common Result<T> pattern & Generic Widgets
├── services/     --> Infrastructure Clients (API, Storage)
├── models/       --> Data transfer models & JSON decoders
├── repositories/ --> Abstract & Concrete Repository layer
├── widgets/      --> Global UI Components (AppCard, StatusBadge, CustomButton)
└── features/     --> Feature Modules (Splash, Auth, Diagnostics, etc.)
    └── presentation/
        ├── controllers/ --> StateNotifiers / Riverpod Providers
        └── views/       --> Declarative Widget UI
```

---

## 5. Database Schema & Migration Guidelines

- **Engine**: PostgreSQL 16 managed asynchronously via `asyncpg`.
- **Primary Keys**: All tables MUST use random UUIDv4 primary keys (`UUIDPrimaryKeyMixin`).
- **Audit Columns**: Every table inherits `TimestampMixin` (`created_at`, `updated_at`).
- **Migration Strategy**: Database changes MUST be versioned using Alembic async scripts located in `backend/alembic/versions/`.

---

## 6. Security Architecture Placeholder

- **Token Format**: JSON Web Tokens (JWT) signed using HMAC-SHA256 (`HS256`).
- **Password Hashing**: Bcrypt algorithm via Passlib context.
- **Header Injection**: Bearer tokens are attached by Dio interceptors on frontend and authenticated via FastAPI dependency guards on backend.

---

## 7. Containerization & Orchestration

- **Production Dockerfile**: Multi-stage build minimizing image footprint.
- **Docker Compose**: Orchestrates FastAPI application, PostgreSQL 16 (healthchecked), and Redis 7 (healthchecked) under `backtrace_network` bridge network.
