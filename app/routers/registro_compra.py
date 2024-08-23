from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from .. import crud, database

router = APIRouter(
    prefix="/registro_compra",
    tags=["registro_compra"],
)

@router.get("/",response_model=List[schemas.RegistroCompraBase])
def read_registros_compra(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    registros = crud.get_registros_compra(db, skip=skip, limit=limit)
    return registros

# estructura de la respuesta JSON, page, total_pages, data en schemas.py
# agregar parametro actions para ver o descargar el archivo como excel
# hacer otro endpoint que acepte filtros para la busqueda, por ejemplo por fechas