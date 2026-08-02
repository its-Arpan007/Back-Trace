import pytest
from app.core.security import get_password_hash, verify_password
from app.core.security.jwt import create_token_pair, decode_token, hash_token


def test_password_hashing():
    password = "SecretPassword123!"
    hashed = get_password_hash(password)
    assert hashed != password
    assert verify_password(password, hashed) is True
    assert verify_password("WrongPassword", hashed) is False


def test_jwt_token_creation_and_decoding():
    user_id = "11111111-1111-1111-1111-111111111111"
    role = "student"
    session_id = "22222222-2222-2222-2222-222222222222"

    access_token, refresh_token, expires = create_token_pair(user_id, role, session_id)

    access_payload = decode_token(access_token)
    assert access_payload["sub"] == user_id
    assert access_payload["role"] == role
    assert access_payload["type"] == "access"

    refresh_payload = decode_token(refresh_token)
    assert refresh_payload["sub"] == user_id
    assert refresh_payload["type"] == "refresh"

    r_hash = hash_token(refresh_token)
    assert len(r_hash) == 64
