from pydantic import BaseModel
from datetime import date

class ExhibitInput(BaseModel):
    id_exhibition: int
    name: str
    category: str
    year_of_creation: date
    author: str

class ExhibitOutput(BaseModel):
    id: int
    id_exhibition: int
    name: str
    category: str
    year_of_creation: date
    author: str
