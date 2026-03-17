from pydantic import BaseModel, EmailStr, field_validator  # Cambio importante
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str

    @field_validator('password')
    @classmethod
    def password_length(cls, v: str) -> str:
        if len(v.encode('utf-8')) > 72:
            raise ValueError('La contraseña no puede exceder 72 bytes')
        return v

class Usuario(UsuarioBase):
    id: int
    activo: bool

    class Config:
        from_attributes = True  # ⚠️ Cambio clave: orm_mode -> from_attributes