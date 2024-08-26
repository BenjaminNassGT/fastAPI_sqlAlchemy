from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

# Base schema with common configurations
class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


# Sociedad Schema
class SociedadBase(ConfiguredBaseModel):
    rut: str
    razon_social: Optional[str] = None
    cliente_id: Optional[int] = None
    estado: Optional[bool] = None


class SociedadCreate(SociedadBase):
    pass


class SociedadUpdate(SociedadBase):
    pass


class Sociedad(SociedadBase):
    id: int
    registros_compra: List["RegistroCompra"] = []

    class Config:
        orm_mode = True


# TipoArchivo Schema
class TipoArchivoBase(ConfiguredBaseModel):
    fuente: Optional[str] = None
    tipo_archivo: Optional[str] = None
    es_reporte: Optional[bool] = False
    es_interno: Optional[bool] = True
    es_externo: Optional[bool] = False


class TipoArchivoCreate(TipoArchivoBase):
    pass


class TipoArchivoUpdate(TipoArchivoBase):
    pass


class TipoArchivo(TipoArchivoBase):
    id: int
    registros_compra: List["RegistroCompra"] = []

    class Config:
        orm_mode = True


# RegistroCompra Schema
class RegistroCompraBase(ConfiguredBaseModel):
    id_sociedad: int
    id_tipo_archivo: int
    periodo: Optional[int] = None
    nro: Optional[int] = None
    tipo_doc: int
    tipo_compra: Optional[str] = None
    rut_proveedor: Optional[str] = None
    razon_social: Optional[str] = None
    folio: int
    fecha_docto: Optional[str] = None
    fecha_recepcion: Optional[str] = None
    fecha_reclamo: Optional[str] = None
    fecha_acuse: Optional[str] = None
    monto_exento: Optional[int] = None
    monto_neto: Optional[int] = None
    monto_iva_recuperable: Optional[int] = None
    monto_iva_no_recuperable: Optional[int] = None
    codigo_iva_no_rec: Optional[int] = None
    monto_total: Optional[int] = None
    monto_neto_activo_fijo: Optional[int] = None
    iva_activo_fijo: Optional[int] = None
    iva_uso_comun: Optional[int] = None
    impto_sin_derecho_a_credito: Optional[int] = None
    iva_no_retenido: Optional[int] = None
    tabacos_puros: Optional[int] = None
    tabacos_cigarrillos: Optional[int] = None
    tabacos_elaborados: Optional[int] = None
    nce_o_nde_sobre_fac_de_compra: Optional[int] = None
    codigo_otro_impuesto: Optional[int] = None
    valor_otro_impuesto: Optional[int] = None
    tasa_otro_impuesto: Optional[int] = None
    fecha_insert: Optional[datetime] = None


class RegistroCompraCreate(RegistroCompraBase):
    pass


class RegistroCompraUpdate(RegistroCompraBase):
    pass


class RegistroCompra(RegistroCompraBase):
    id: int
    sociedad: Optional[Sociedad] = None
    tipo_archivo: Optional[TipoArchivo] = None

    class Config:
        orm_mode = True
