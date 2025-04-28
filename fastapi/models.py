from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Integer, Float, Boolean, text

class Shipment(Base):
    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True, index=True)
    bl_num = Column(String)
    cnee = Column(String)
    notify = Column(String)
    pod = Column(String)
    pol = Column(String)
    vessel = Column(String)
    voyage = Column(String)
    cargo_weight = Column(Float)
    released = Column(Boolean)
    tel_num = Column(Integer, (10))
    create_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))




