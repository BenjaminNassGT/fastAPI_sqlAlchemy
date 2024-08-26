from typing import List
from sqlalchemy.orm import Session
from app import schemas
from ..repository import registros as registrosRepository

def fetch_registros_compra(
    db: Session, 
    skip: int = 0, 
    limit: int = 10, 
) -> List[schemas.RegistroCompraBase]:
    registros = registrosRepository.get_registros_compra(db, skip, limit)
    return [schemas.RegistroCompraBase.model_validate(registro) for registro in registros]


# estructura de la respuesta JSON, page, total_pages, data en schemas.py
# agregar parametro actions para ver o descargar el archivo como excel
# hacer otro endpoint que acepte filtros para la busqueda, por ejemplo por fechas