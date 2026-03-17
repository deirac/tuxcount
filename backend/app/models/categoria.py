# app/models/categoria.py

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from app.database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    nombre = Column(String(50), nullable=False)
    tipo = Column(Enum("ingreso", "gasto"), nullable=False)
    es_fijo = Column(Boolean, default=False)
    color = Column(String(7), nullable=True)  # Código hexadecimal, ej: #FF5733
    icono = Column(String(50), nullable=True)  # Nombre del icono (ej: "comida", "transporte")
    activo = Column(Boolean, default=True)

    # Relaciones
    usuario = relationship("Usuario", back_populates="categorias")
    transacciones = relationship("Transaccion", back_populates="categoria", cascade="all, delete-orphan")
    plantillas_fijas = relationship("PlantillaFijo", back_populates="categoria")
    presupuestos = relationship("Presupuesto", back_populates="categoria")