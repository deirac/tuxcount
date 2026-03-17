# app/models/transaccion.py

from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Date, DateTime, Text, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Transaccion(Base):
    __tablename__ = "transacciones"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    cuenta_id = Column(Integer, ForeignKey("cuentas.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=True)
    fecha = Column(Date, nullable=False)
    descripcion = Column(String(255), nullable=True)
    monto = Column(Numeric(10, 2), nullable=False)
    tipo = Column(Enum("ingreso", "gasto", "transferencia"), nullable=False)
    es_pagado = Column(Boolean, default=True)
    fecha_programada = Column(Date, nullable=True)
    transferencia_destino_cuenta_id = Column(Integer, ForeignKey("cuentas.id"), nullable=True)
    notas = Column(Text, nullable=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    es_fijo = Column(Boolean, default=False)

    # Relaciones

    # Usuario
    usuario = relationship("Usuario", back_populates="transacciones")
    
    # Categoría (para ingresos y gastos)
    categoria = relationship("Categoria", back_populates="transacciones")
    
    # Cuentas
    cuenta = relationship(
        "Cuenta",
        foreign_keys=[cuenta_id],  # <-- Especificado
        back_populates="transacciones"
    )

    cuenta_destino = relationship(
        "Cuenta",
        foreign_keys=[transferencia_destino_cuenta_id],  # <-- Especificado
        back_populates="transferencias_recibidas"
    )

    # Relaciones con otras tablas (opcionales, se agregarán cuando existan)
        # Relación con PagoDeuda (uno a uno, opcional)
    pago_deuda = relationship(
        "PagoDeuda",
        back_populates="transaccion",
        uselist=False,          # Una transacción puede tener un solo pago deuda asociado
        cascade="all, delete-orphan"
    )

    # Relación con AporteAhorro (uno a uno, opcional)
    aporte_ahorro = relationship(
        "AporteAhorro",
        back_populates="transaccion",
        uselist=False,
        cascade="all, delete-orphan"
    )
