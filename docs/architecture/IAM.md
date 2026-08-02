# BACKTRACE Identity & Access Management (IAM) Documentation

## 1. Overview & Architecture
The BACKTRACE IAM system provides a production-grade security, identity, session management, and Role-Based Access Control (RBAC) foundation across the platform.

```
+------------------+         +---------------------+         +---------------------+
| Flutter Frontend | ------> |  FastAPI IAM Router | ------> |  PostgreSQL Storage |
| (Riverpod/Dio)   |  JWT    |  (/auth, /profile)  |         | (Users, Profiles,   |
+------------------+         +---------------------+         |  Sessions, Audits)  |
                                                             +---------------------+
```

---

## 2. User Roles & RBAC Matrix
1. **Student (`student`)**: Access diagnostic engines, submit answers, view personal mastery & recommendations.
2. **Teacher (`teacher`)**: View class analytics, assign question sets, inspect student diagnostic reports.
3. **Administrator (`admin`)**: Access system configuration, manage users, configure feature flags & plugins.

---

## 3. Database Entity-Relationship Schema

```
UserModel (users)
├── StudentProfileModel (1:1)
├── TeacherProfileModel (1:1)
├── AdminProfileModel (1:1)
├── SessionModel (1:N)
│   └── RefreshTokenModel (1:N)
├── AuditLogModel (1:N)
└── UserPreferencesModel (1:1)
```

---

## 4. Authentication Sequence Flow

1. **User Registration** (`POST /auth/register`): Hashes password via Bcrypt, creates `users` record and role-specific profile (`student_profiles`, `teacher_profiles`, or `admin_profiles`).
2. **User Login** (`POST /auth/login`): Verifies password, creates active `SessionModel`, mints Access Token (short-lived) + Refresh Token (long-lived), records `USER_LOGGED_IN` in `audit_logs`.
3. **Token Refresh** (`POST /auth/refresh`): Enforces Token Rotation. Revokes previous refresh token hash and issues new token pair.
4. **Logout** (`POST /auth/logout`): Revokes current session and invalidates active refresh tokens.
