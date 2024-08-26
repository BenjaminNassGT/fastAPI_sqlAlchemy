from typing import List
from sqlalchemy.orm import Session
from app import schemas
from ..repository import registros as registrosRepository


def fetch_registros_compra_with_filters(
    db: Session, 
    skip: int = 0, 
    limit: int = 10, 
    id_sociedad: int = None
) -> List[schemas.RegistroCompraBase]:
    filters = {}
    if id_sociedad:
        filters['id_sociedad'] = id_sociedad
    
    registros = registrosRepository.get_registros_compra_by_filter(db, skip, limit, **filters)
    return [schemas.RegistroCompraBase.model_validate(registro) for registro in registros]
