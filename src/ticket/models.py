from pydantic import BaseModel
from datetime import time, date

class TicketInput(BaseModel):
    id_museum: int
    id_exhibition: int
    id_visitor: int
    name: str
    date: date
    time: time
    ticket_price: float


class TicketOutput(BaseModel):
    id: int
    id_museum: int
    id_exhibition: int
    id_visitor: int
    name: str
    date: date
    time: time
    ticket_price: float

