
from pydantic import BaseModel
from datetime import datetime

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
    status: int
    user_id: int
    categories_id: int
