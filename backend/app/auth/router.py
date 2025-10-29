from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from ..db import SessionLocal, init_db
from ..db.models import User
from .utils import hash_password, verify_password, create_token

router = APIRouter(prefix='/auth', tags=['auth'])
def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

class RegisterReq(BaseModel):
    email: EmailStr
    password: str
class LoginReq(BaseModel):
    email: EmailStr
    password: str

@router.on_event('startup')
def _init(): init_db()

@router.post('/register')
def register(req: RegisterReq, db: Session = Depends(get_db)):
    if db.query(User).filter_by(email=req.email).first():
        raise HTTPException(status_code=400, detail='Email already registered')
    user = User(email=req.email, password_hash=hash_password(req.password))
    db.add(user); db.commit(); db.refresh(user)
    token = create_token(user.id, user.email)
    return {'ok': True, 'token': token, 'plan': user.plan}

@router.post('/login')
def login(req: LoginReq, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=req.email).first()
    if not user or not verify_password(req.password, user.password_hash):
        raise HTTPException(status_code=401, detail='Invalid credentials')
    token = create_token(user.id, user.email)
    return {'ok': True, 'token': token, 'plan': user.plan}
