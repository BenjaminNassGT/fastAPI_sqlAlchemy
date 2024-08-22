from sqlalchemy import Column, Integer, String, BigInteger, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Sociedad(Base):
    __tablename__ = 'sociedad'

    id = Column(Integer, primary_key=True)
    rut = Column(String(12), nullable=False)
    razon_social = Column(String(100))
    cliente_id = Column(Integer)
    estado = Column(Boolean)

    # Relationship to RegistroCompra
    registros_compra = relationship("RegistroCompra", back_populates="sociedad")

    def __repr__(self):
        return f"<Sociedad(id={self.id}, rut={self.rut}, razon_social={self.razon_social})>"

class TipoArchivo(Base):
    __tablename__ = 'tipo_archivo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fuente = Column(String(50))
    tipo_archivo = Column(String(100))
    es_reporte = Column(Boolean, default=False, nullable=False)
    es_interno = Column(Boolean, default=True)
    es_externo = Column(Boolean, default=False)

    # Relationship to RegistroCompra
    registros_compra = relationship("RegistroCompra", back_populates="tipo_archivo")

    def __repr__(self):
        return f"<TipoArchivo(id={self.id}, tipo_archivo={self.tipo_archivo})>"

class RegistroCompra(Base):
    __tablename__ = 'registro_compra'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_sociedad = Column(Integer, ForeignKey('sociedad.id'), nullable=False)
    id_tipo_archivo = Column(Integer, ForeignKey('tipo_archivo.id'), nullable=False)
    periodo = Column(BigInteger)
    nro = Column(BigInteger)
    tipo_doc = Column(BigInteger, nullable=False)
    tipo_compra = Column(String)
    rut_proveedor = Column(String)
    razon_social = Column(String)
    folio = Column(BigInteger, nullable=False)
    fecha_docto = Column(String)
    fecha_recepcion = Column(String)
    fecha_reclamo = Column(String(100))
    fecha_acuse = Column(String)
    monto_exento = Column(BigInteger)
    monto_neto = Column(BigInteger)
    monto_iva_recuperable = Column(BigInteger)
    monto_iva_no_recuperable = Column(BigInteger)
    codigo_iva_no_rec = Column(BigInteger)
    monto_total = Column(BigInteger)
    monto_neto_activo_fijo = Column(BigInteger)
    iva_activo_fijo = Column(BigInteger)
    iva_uso_comun = Column(BigInteger)
    impto_sin_derecho_a_credito = Column(BigInteger)
    iva_no_retenido = Column(BigInteger)
    tabacos_puros = Column(BigInteger)
    tabacos_cigarrillos = Column(BigInteger)
    tabacos_elaborados = Column(BigInteger)
    nce_o_nde_sobre_fac_de_compra = Column(BigInteger)
    codigo_otro_impuesto = Column(BigInteger)
    valor_otro_impuesto = Column(BigInteger)
    tasa_otro_impuesto = Column(BigInteger)
    fecha_insert = Column(DateTime, default=datetime.utcnow)

    # Relationships
    sociedad = relationship("Sociedad", back_populates="registros_compra")
    tipo_archivo = relationship("TipoArchivo", back_populates="registros_compra")

    def __repr__(self):
        return f"<RegistroCompra(id={self.id}, folio={self.folio}, monto_total={self.monto_total})>"
