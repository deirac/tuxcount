# app/models/usuario.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    activo = Column(Boolean, default=True)

    # Relaciones (usamos strings para evitar importaciones circulares)
    cuentas = relationship("Cuenta", back_populates="usuario", cascade="all, delete-orphan")
    categorias = relationship("Categoria", back_populates="usuario", cascade="all, delete-orphan")
    transacciones = relationship("Transaccion", back_populates="usuario", cascade="all, delete-orphan")
    deudas = relationship("Deuda", back_populates="usuario", cascade="all, delete-orphan")
    metas_ahorro = relationship("MetaAhorro", back_populates="usuario", cascade="all, delete-orphan")
    presupuestos = relationship("Presupuesto", back_populates="usuario", cascade="all, delete-orphan")
    plantillas_fijas = relationship("PlantillaFijo", back_populates="usuario", cascade="all, delete-orphan")