import hashlib
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional, Tuple
import jwt
from app.config.jwt import jwt_settings


def create_token_pair(
    user_id: str, role: str, session_id: str
) -> Tuple[str, str, datetime]:
    now = datetime.now(timezone.utc)
    access_token_expires = now + timedelta(minutes=jwt_settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = now + timedelta(days=jwt_settings.REFRESH_TOKEN_EXPIRE_DAYS)

    access_payload = {
        "sub": user_id,
        "role": role,
        "session_id": session_id,
        "type": "access",
        "exp": access_token_expires,
        "iat": now,
    }
    access_token = jwt.encode(
        access_payload, jwt_settings.SECRET_KEY, algorithm=jwt_settings.ALGORITHM
    )

    refresh_payload = {
        "sub": user_id,
        "session_id": session_id,
        "type": "refresh",
        "exp": refresh_token_expires,
        "iat": now,
    }
    refresh_token = jwt.encode(
        refresh_payload, jwt_settings.SECRET_KEY, algorithm=jwt_settings.ALGORITHM
    )

    return access_token, refresh_token, refresh_token_expires


def hash_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


def decode_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(
            token, jwt_settings.SECRET_KEY, algorithms=[jwt_settings.ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
