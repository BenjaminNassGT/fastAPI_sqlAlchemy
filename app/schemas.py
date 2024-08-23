# agregar schema de registro_compra, sociedad y tipo_archivo con pydantic
from pydantic import BaseModel
from typing import List, Optional

class RegistroCompraBase(BaseModel):
    id_sociedad: Optional[int]=None
    id_tipo_archivo: int
    periodo: int
    nro: int
    tipo_doc: int
    tipo_compra: str
    rut_proveedor: str
    razon_social: str
    folio: int
    fecha_docto: str
    fecha_recepcion: str
    fecha_reclamo: str
    fecha_acuse: str
    monto_exento: int
    monto_neto: int
    monto_iva_recuperable: int
    monto_iva_no_recuperable: int
    codigo_iva_no_rec: int
    monto_total: int
    monto_neto_activo_fijo: int
    iva_activo_fijo: int
    iva_uso_comun: int
    impto_sin_derecho_a_credito: int
    iva_no_retenido: int
    tabacos_puros: int
    tabacos_cigarrillos: int
    tabacos_elaborados: int
    nce_o_nde_sobre_fac_de_compra: int
