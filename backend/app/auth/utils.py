from passlib.hash import bcrypt
from datetime import datetime, timedelta
import jwt
from ..config import JWT_SECRET, JWT_ALGO
def hash_password(p:str)->str: return bcrypt.hash(p)
def verify_password(p:str,h:str)->bool: return bcrypt.verify(p,h)
def create_token(user_id:int, email:str)->str:
    payload = {'sub': str(user_id), 'email': email, 'exp': datetime.utcnow()+timedelta(days=7)}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)
def decode_token(t:str): return jwt.decode(t, JWT_SECRET, algorithms=[JWT_ALGO])
