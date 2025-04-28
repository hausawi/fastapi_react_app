import datetime
from pydentic import BaseModel
import models as models


class ShipmentBase(BaseModel):
    bl_num : str
    shipper : str
    cnee: str
    notify: str
    pod: str
    pol: str
    vessel: str
    voyage: str
    cargo_weight: str
    released: bool

class ShipmentModels(ShipmentBase):
    id: int
    created_at: datetime
    tel_num: int
    email: str
    class config():
        orm_mode = True

