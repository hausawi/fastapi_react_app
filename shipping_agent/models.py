from database import Base
from sqlalchemy import TIMESTAMP, Column, String, Integer, Float, Boolean, text

class Shippment(Base):
    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True, index=True)
    bl_num = Column(String)
    cnee = Column(String)
    notify = Column(String)
    good_des = Column(String)
    pod = Column(String)
    pol = Column(String)
    eta = Column(String)
    etd = Column(String)
    net_weight = Column(Float)
    voyage_name = Column(String)
    voyage_num = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))



