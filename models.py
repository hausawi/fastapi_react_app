from database import Base
from sqlalchemy import Column, String, Integer, Float, Boolean

class Shippment(Base):
    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True, index=True)
    bl_num = Column(String)
    cnee = Column(String)
    notify = Column(String)
    good_des = Column(String)
    eta = Column(String)
    etd = Column(String)
    net_weight = Column(Float)
    recieved = Column(Boolean)


