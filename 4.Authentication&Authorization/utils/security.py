from datetime import datetime, timedelta
from typing import Optional

from core.config import settings
from jose import jwt

# Patch bcrypt to fix compatibility issue with passlib
try:
    import bcrypt
    if not hasattr(bcrypt, '__about__'):
        import types
        bcrypt.__about__ = types.SimpleNamespace(__version__="5.0.0")
except ImportError:
    pass

# Import bcrypt directly for password operations
import bcrypt


def _truncate_password(password: str, max_length: int = 72) -> bytes:
    """Truncate password to specified length to comply with bcrypt limitations"""
    password_bytes = password.encode('utf-8')
    if len(password_bytes) > max_length:
        return password_bytes[:max_length]
    return password_bytes


def hash_password(password: str) -> str:
    # Truncate password to 72 bytes for bcrypt compatibility
    truncated_password = _truncate_password(password, 72)
    # Use bcrypt directly instead of through passlib to avoid length checking
    hashed = bcrypt.hashpw(truncated_password, bcrypt.gensalt())
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Truncate password to 72 bytes for bcrypt compatibility
    truncated_password = _truncate_password(plain_password, 72)
    # Use bcrypt directly instead of through passlib to avoid length checking
    return bcrypt.checkpw(truncated_password, hashed_password.encode('utf-8'))


def create_access_token(subject: str, role: str, expires_delta: Optional[timedelta] = None) -> str:
    now = datetime.utcnow()
    expire = now + (expires_delta or timedelta(minutes=settings.access_token_expire_minutes))
    to_encode = {"exp": expire, "iat": now, "sub": str(subject), "role": role}
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)


def decode_token(token: str) -> dict:
    return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])