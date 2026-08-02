# BACKTRACE - AI-Powered Learning Intelligence Platform

> **BACKTRACE is NOT an AI chatbot.**
> BACKTRACE is an AI-powered Learning Intelligence Platform that diagnoses the root cause behind every wrong answer.

---

## 🚀 Overview & Philosophy

Traditional learning platforms treat incorrect answers superficially—offering static solution steps or simple correct/incorrect markers. **BACKTRACE** takes a fundamental diagnostic approach. It reverse-engineers student errors to uncover underlying misconceptions, missing prerequisites, cognitive slips, or knowledge gaps across a dynamic knowledge graph.

Phase 1 establishes the production-grade, highly scalable, and modular clean architecture foundation for both the Flutter frontend and FastAPI backend.

---

## 🛠️ Architecture & Tech Stack

### Frontend (Flutter Clean Architecture)
- **Framework**: Flutter (Dart 3.0+)
- **State Management**: Riverpod (`flutter_riverpod`)
- **Routing**: GoRouter (`go_router`)
- **HTTP Client**: Dio (`dio`) with custom Interceptors & Logging
- **Data Models**: Freezed (`freezed_annotation`) & Json Serializable
- **Design System**: Tailored HSL color palette, Google Fonts (`Inter` / `Outfit`), dark/light theme tokens, micro-animations, and glassmorphism.

### Backend (FastAPI Production Architecture)
- **Framework**: FastAPI (Python 3.13)
- **ORM / Database**: SQLAlchemy 2.0 (Asyncpg) & PostgreSQL 16
- **Migration Engine**: Alembic (Async workflow)
- **Caching & State**: Redis 7
- **Security**: JWT & Passlib (Bcrypt) placeholders
- **Testing**: Pytest & Pytest-Asyncio with HTTPX AsyncClient

### DevOps & Infrastructure
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions pipeline for automated linting & testing
- **Environment**: Centralized `.env` configuration

---

## 📂 Project Structure

```
BACKTRACE/
├── frontend/                  # Flutter Clean Architecture App
│   ├── lib/
│   │   ├── core/              # Config, Theme, Network (Dio), Errors, DI, Constants
│   │   ├── shared/            # Reusable UI widgets & Result type
│   │   ├── features/          # Feature modules (Splash, Auth, Diagnostics, etc.)
│   │   ├── services/          # Infrastructure services (Storage, API)
│   │   ├── models/            # Domain & DTO data models
│   │   ├── repositories/      # Base repository contracts & implementations
│   │   ├── widgets/           # Global design system widgets
│   │   ├── theme/             # Light & Dark theme tokens, typography, colors
│   │   ├── routes/            # GoRouter navigation setup & constants
│   │   └── utils/             # Formatters, loggers, extensions
│   └── pubspec.yaml
│
├── backend/                   # FastAPI Production Server
│   ├── app/
│   │   ├── api/               # API Router & v1 endpoints (Health & Module Placeholders)
│   │   ├── core/              # Security, Config, Logging, Exceptions
│   │   ├── database/          # Async SQLAlchemy Engine & Session Provider
│   │   ├── models/            # Base Declarative Models & UUID Mixins
│   │   ├── schemas/           # Pydantic DTOs & API Envelope
│   │   ├── services/          # Business logic services & Redis client
│   │   ├── repositories/      # Generic Async Repository (CRUD)
│   │   ├── middlewares/       # Request ID & Logging Middlewares
│   │   └── utils/             # Loggers & Helpers
│   ├── alembic/               # Database Migration System
│   ├── tests/                 # Pytest test suite & fixtures
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml         # Container Orchestration
├── .github/workflows/ci.yml   # CI/CD Workflow
├── ARCHITECTURE.md            # Comprehensive System Architecture Specification
└── README.md
```

---

## ⚡ Quick Start

### 1. Run via Docker Compose (Recommended)

To launch the complete platform (FastAPI Backend, PostgreSQL, and Redis):

```bash
# Clone repository
git clone https://github.com/your-org/backtrace.git
cd backtrace

# Start containers
docker-compose up --build
```

Access the API documentation at:
- Swagger UI: `http://localhost:8000/api/v1/docs`
- ReDoc: `http://localhost:8000/api/v1/redoc`

---

### 2. Local Backend Execution

```bash
cd backend

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload --port 8000
```

---

### 3. Running Backend Tests

```bash
cd backend
pytest -v tests/
```

---

### 4. Running Flutter Frontend

```bash
cd frontend

# Install Flutter packages
flutter pub get

# Run Flutter app
flutter run
```

---

## 🔮 Future Modules Roadmap

The architecture is prepared for seamless expansion across:
1. **Authentication & Identity**
2. **Knowledge Graph Module**
3. **Question Engine**
4. **Diagnostic Engine**
5. **Mastery Engine**
6. **Recommendation Engine**
7. **Analytics Engine**
8. **Teacher Dashboard**
9. **Admin Dashboard**

---

## 📄 License

Copyright © 2026 BACKTRACE Engineering. All rights reserved.
