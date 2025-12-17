import jwt
from datetime import datetime, timedelta
from django.conf import settings

ACCESS_TOKEN_EXP_MINUTES = 30

def generate_access_token(user):
    payload = {
        "user_id": user.id,
        "email": user.email,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXP_MINUTES),
        "iat": datetime.utcnow()
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
