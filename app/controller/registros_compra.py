from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import database, schemas
from app.service import registro_compra, registro_compra_filtros

router = APIRouter(
    prefix="/registro_compra",
    tags=["registro_compra"],
)

@router.get("/", response_model=List[schemas.RegistroCompraBase])
def fetch_registros_compra(
    db: Session = Depends(database.get_db), 
    skip: int = 0, 
    limit: int = 10, 
):
    try:
        return registro_compra.fetch_registros_compra(db, skip, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/filtros", response_model=List[schemas.RegistroCompraBase])
def fetch_registros_compra_with_filters(
    db: Session = Depends(database.get_db), 
    skip: int = 0, 
    limit: int = 10, 
    id_sociedad: int = None
):
    try:
        return registro_compra_filtros.fetch_registros_compra_with_filters(db, skip, limit, id_sociedad)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
