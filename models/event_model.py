from pydantic import BaseModel
from datetime import datetime
#clase Event creada para pintar eventos, pendiente clase EventCreate para crear eventos
class Event(BaseModel):
    id: int
    title: str
    description: str
    date: datetime
    price: float
    capacity: int
    address: str
    latitude: float
    longitude: float
    image: str
    status: bool
    categories_id: int
    users_id: int



    