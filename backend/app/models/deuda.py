# app/models/deuda.py

from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Date, Enum, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Deuda(Base):
    __tablename__ = "deudas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    tipo = Column(Enum("deuda_a_pagar", "deuda_a_cobrar"), nullable=False)
    descripcion = Column(String(255), nullable=False)
    monto_original = Column(Numeric(10, 2), nullable=False)
    saldo_restante = Column(Numeric(10, 2), nullable=False)
    tasa_interes = Column(Numeric(5, 2), default=0)
    fecha_inicio = Column(Date, nullable=False)
    fecha_vencimiento = Column(Date, nullable=True)
    periodicidad_pago = Column(Enum("mensual", "quincenal", "semanal"), nullable=True)
    cuota_periodica = Column(Numeric(10, 2), nullable=True)
    cuenta_id_asociada = Column(Integer, ForeignKey("cuentas.id"), nullable=True)
    activo = Column(Boolean, default=True)

    # Relaciones
    usuario = relationship("Usuario", back_populates="deudas")
    cuenta_asociada = relationship("Cuenta", foreign_keys=[cuenta_id_asociada], back_populates="deudas")
    pagos = relationship("PagoDeuda", back_populates="deuda", cascade="all, delete-orphan")
