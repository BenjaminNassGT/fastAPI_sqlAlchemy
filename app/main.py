from fastapi import FastAPI

from .controller import registros_compra

from .database import Base, engine

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(registros_compra.router)


