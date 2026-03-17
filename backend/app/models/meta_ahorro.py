# app/models/meta_ahorro.py

from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Date, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class MetaAhorro(Base):
    __tablename__ = "metas_ahorro"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    nombre = Column(String(100), nullable=False)
    monto_objetivo = Column(Numeric(10, 2), nullable=False)
    monto_actual = Column(Numeric(10, 2), default=0)
    fecha_limite = Column(Date, nullable=True)
    cuenta_id = Column(Integer, ForeignKey("cuentas.id"), nullable=False)
    prioridad = Column(Integer, default=3)  # 1 (muy alta) a 5 (baja)
    activo = Column(Boolean, default=True)

    # Relaciones
    usuario = relationship("Usuario", back_populates="metas_ahorro")
    cuenta = relationship("Cuenta", back_populates="metas")
    aportaciones = relationship("AporteAhorro", back_populates="meta", cascade="all, delete-orphan")
