from fastapi import FastAPI, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session # type: ignore
from fastapi.middleware.cors import CORSMiddleware
import schemas, models
from database import get_db

app = FastAPI()

origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/shipments/", response_models=schemas.ShipmentModels)
def create_shipment(db:db_dependency, shipments:schemas.ShipmentBase):
    db_shipments = models.Shipment(**shipments.dict())
    db.add(db_shipments)
    db.commit()
    db.refresh(db_shipments)
    return db_shipments
