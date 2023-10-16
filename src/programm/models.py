from pydantic import BaseModel
from datetime import date

class ProgrammInput(BaseModel):
    id_museum: int
    name: str
    date: date
    description: str


class ProgrammOutput(BaseModel):
    id: int
    id_museum: int
    name: str
    date: date
    description: str
