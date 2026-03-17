# app/models/cuenta.py

from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Date, Text, Boolean, Enum
from sqlalchemy.orm import relationship
from app.database import Base

class Cuenta(Base):
    __tablename__ = "cuentas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    nombre = Column(String(50), nullable=False)
    tipo = Column(
        Enum("efectivo", "cuenta_corriente", "ahorro", "tarjeta_credito", "inversion"),
        nullable=False
    )
    saldo_inicial = Column(Numeric(10, 2), default=0)
    moneda = Column(String(3), default="COP")
    fecha_apertura = Column(Date, nullable=False)
    notas = Column(Text, nullable=True)
    incluir_en_patrimonio = Column(Boolean, default=True)

    # Relaciones
    usuario = relationship("Usuario", back_populates="cuentas")
    transacciones = relationship("Transaccion", back_populates="cuenta", cascade="all, delete-orphan")
    # Relación para transferencias (cuando es cuenta destino)
    transferencias_recibidas = relationship(
        "Transaccion",
        foreign_keys="[Transaccion.transferencia_destino_cuenta_id]",
        back_populates="cuenta_destino"
    )
    # Relación con deudas (cuenta asociada)
    deudas = relationship("Deuda", back_populates="cuenta_asociada")
    # Relación con metas de ahorro
    metas = relationship("MetaAhorro", back_populates="cuenta")
