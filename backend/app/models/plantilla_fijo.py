# app/models/plantilla_fijo.py

from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Date, Boolean, Enum
from sqlalchemy.orm import relationship
from app.database import Base

class PlantillaFijo(Base):
    __tablename__ = "plantillas_fijas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    cuenta_id = Column(Integer, ForeignKey("cuentas.id"), nullable=False)
    descripcion = Column(String(255), nullable=False)
    monto = Column(Numeric(10, 2), nullable=False)
    tipo = Column(Enum("ingreso", "gasto"), nullable=False)
    periodicidad = Column(Enum("mensual", "quincenal", "semanal", "anual"), nullable=False)
    dia_periodo = Column(Integer, nullable=False)  # Día del mes/semana (ej. 15 para mensual)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=True)
    activo = Column(Boolean, default=True)
    ultima_generacion = Column(Date, nullable=True)

    # Relaciones
    usuario = relationship("Usuario", back_populates="plantillas_fijas")
    categoria = relationship("Categoria", back_populates="plantillas_fijas")
    cuenta = relationship("Cuenta", back_populates="plantillas_fijas")
   
