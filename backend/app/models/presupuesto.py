# app/models/presupuesto.py

from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class Presupuesto(Base):
    __tablename__ = "presupuestos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    mes = Column(Integer, nullable=False)  # 1-12
    anio = Column(Integer, nullable=False)
    monto_limite = Column(Numeric(10, 2), nullable=False)
    notas = Column(Text, nullable=True)

    # Restricción: un usuario no puede tener dos presupuestos para la misma categoría en el mismo mes/año
    __table_args__ = (
        UniqueConstraint('usuario_id', 'categoria_id', 'mes', 'anio', name='unique_presupuesto_por_mes'),
    )

    # Relaciones
    usuario = relationship("Usuario", back_populates="presupuestos")
    categoria = relationship("Categoria", back_populates="presupuestos")
