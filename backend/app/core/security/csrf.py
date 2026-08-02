import hmac
import hashlib


def generate_csrf_token(secret: str, session_id: str) -> str:
    return hmac.new(secret.encode(), session_id.encode(), hashlib.sha256).hexdigest()


def verify_csrf_token(token: str, secret: str, session_id: str) -> bool:
    expected = generate_csrf_token(secret, session_id)
    return hmac.compare_digest(token, expected)
