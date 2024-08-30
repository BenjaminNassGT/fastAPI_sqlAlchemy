from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import database, schemas
from app.service import registro_compra, registro_compra_filtros, registro_joins

router = APIRouter(
    prefix="/registro_compra",
    tags=["registro_compra"],
)

@router.get("/")
def fetch_registros_compra(
    db: Session = Depends(database.get_db), 
    skip: int = 0, 
    limit: int = 10, 
    action: str = 'view'
):
    try:
        return registro_compra.fetch_registros_compra(db, skip, limit, action)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/join")
def controller_get_registros_join(
    db: Session = Depends(database.get_db), 
    skip: int = 0, 
    limit: int = 10, 
    action: str = 'view'
):
    try:
        return registro_joins.service_get_registros_join(db, skip, limit, action)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/join_separate")
def controller_get_registros_join_en_df(
    db: Session = Depends(database.get_db), 
    skip: Optional[int] = None, 
    limit: Optional[int] = None,
    action: str = 'view'
):
    try:
        return registro_joins.service_get_registros_join_en_df(db, skip, limit, action)
    except Exception as e:
        print(e)
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
