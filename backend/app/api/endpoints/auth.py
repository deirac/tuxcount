from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario as UsuarioModel
from app.schemas.usuario import Usuario, UsuarioCreate
from app.schemas.token import Token
from app.api.deps import get_current_user
from datetime import timedelta
from app.core.security import (
    verify_password,
    create_access_token,
    get_password_hash,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/register", response_model=Token)
def register(user_data: UsuarioCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe (usando el modelo SQLAlchemy)
    db_user = db.query(UsuarioModel).filter(UsuarioModel.email == user_data.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Crear nuevo usuario (instancia del modelo SQLAlchemy)
    hashed = get_password_hash(user_data.password)
    new_user = UsuarioModel(
        nombre=user_data.nombre,
        email=user_data.email,
        password_hash=hashed
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Generar token
    access_token = create_access_token(
        data={"sub": new_user.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Buscar usuario por email (usando el modelo SQLAlchemy)
    user = db.query(UsuarioModel).filter(UsuarioModel.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=Usuario)
def read_users_me(current_user: UsuarioModel = Depends(get_current_user)):
    """
    Devuelve la información del usuario autenticado.
    """
    return current_user