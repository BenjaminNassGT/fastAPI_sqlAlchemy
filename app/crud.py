from fastapi import logger
from sqlalchemy.orm import Session
from sqlalchemy import asc
from . import models

def get_registros_compra(db: Session, skip: int = 0, limit: int = 10):
    try:
        # Modify the query to include an ORDER BY clause
        query = db.query(models.RegistroCompra).order_by(models.RegistroCompra.id).offset(skip).limit(limit)
        registros = query.all()
        return registros
    except Exception as e:
        logger.error(f"Error fetching registros_compra: {e}")
        raise

# metodo con filtros