# app/models/pago_deuda.py

from sqlalchemy import Column, Integer, ForeignKey, Numeric, Date, Text
from sqlalchemy.orm import relationship
from app.database import Base

class PagoDeuda(Base):
    __tablename__ = "pagos_deudas"

    id = Column(Integer, primary_key=True, index=True)
    deuda_id = Column(Integer, ForeignKey("deudas.id"), nullable=False)
    fecha_pago = Column(Date, nullable=False)
    monto_pagado = Column(Numeric(10, 2), nullable=False)
    intereses_pagados = Column(Numeric(10, 2), default=0)
    saldo_restante_despues = Column(Numeric(10, 2), nullable=False)
    notas = Column(Text, nullable=True)
    transaccion_id = Column(Integer, ForeignKey("transacciones.id"), nullable=True)

    # Relaciones
    deuda = relationship("Deuda", back_populates="pagos")
    transaccion = relationship("Transaccion", backref="pago_deuda", uselist=False)
