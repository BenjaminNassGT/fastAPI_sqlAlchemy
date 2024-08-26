from fastapi import logger
from sqlalchemy.orm import Session
from sqlalchemy import asc
from .. import models

def get_registros_compra(db: Session, skip: int = 0, limit: int = 10):
    try:
        query = db.query(models.RegistroCompra).order_by(models.RegistroCompra.id).offset(skip).limit(limit)
        registros = query.all()
        return registros
    except Exception as e:
        logger.error(f"Error fetching registros_compra: {e}")
        raise


def get_registros_compra_by_filter(db: Session, skip: int = 0, limit: int = 10, **filters):
    query = db.query(models.RegistroCompra)
    
    # Apply filters
    for key, value in filters.items():
        query = query.filter(getattr(models.RegistroCompra, key) == value)
    
    query = query.order_by(asc(models.RegistroCompra.id)).offset(skip).limit(limit)
    return query.all()

