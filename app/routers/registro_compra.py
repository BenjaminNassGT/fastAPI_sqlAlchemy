from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, crud, database

router = APIRouter(
    prefix="/registro_compra",
    tags=["registro_compra"],
)

@router.get("/")
def read_registros_compra(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    registros = crud.get_registros_compra(db, skip=skip, limit=limit)
    return registros
