from fastapi import logger
from sqlalchemy.orm import Session
from .. import models

def get_tipo_archivos(db: Session, skip: int = None, limit: int = None):
    try:
        query = db.query(models.TipoArchivo)
        
        if skip is not None:
            query = query.offset(skip)
        
        if limit is not None:
            query = query.limit(limit)

        return query
    except Exception as e:
        logger.error(f"Error fetching tipo_archivos: {e}")
        raise e
