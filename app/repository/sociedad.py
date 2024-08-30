from fastapi import logger
from sqlalchemy.orm import Session
from .. import models

def get_sociedades(db: Session, skip: int = None, limit: int = None):
    try:
        query = db.query(models.Sociedad)
        
        if skip is not None:
            query = query.offset(skip)
        
        if limit is not None:
            query = query.limit(limit)
        
        return query
    except Exception as e:
        logger.error(f"Error fetching sociedad: {e}")
        raise e