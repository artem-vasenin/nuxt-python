import jwt
from passlib.context import CryptContext
from datetime import timezone, datetime, timedelta

from app.core.settings import Settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = Settings() # type: ignore[call-arg]

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def add_token(pid: int) -> str:
    expire_time = datetime.now(timezone.utc) + timedelta(minutes=settings.auth.time)
    payload = {'sub': f'{pid}', 'exp': expire_time}
    return jwt.encode(payload, settings.auth.secret, algorithm='HS256')

def check_token(token: str) -> int | None:
    try:
        payload = jwt.decode(token, settings.auth.secret, algorithms=['HS256'])
        return payload['sub']
    except (jwt.PyJWTError, ValueError, KeyError) as e:
        print(e)
        return None