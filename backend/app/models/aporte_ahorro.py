# app/models/aporte_ahorro.py

from sqlalchemy import Column, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from app.database import Base

class AporteAhorro(Base):
    __tablename__ = "aportes_ahorro"

    id = Column(Integer, primary_key=True, index=True)
    meta_id = Column(Integer, ForeignKey("metas_ahorro.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    monto = Column(Numeric(10, 2), nullable=False)
    transaccion_id = Column(Integer, ForeignKey("transacciones.id"), nullable=True)

    # Relaciones
    meta = relationship("MetaAhorro", back_populates="aportaciones")
    transaccion = relationship("Transaccion")  # Relación simple, sin back_populates aún