from pydantic import BaseModel
from datetime import datetime

class ExhibitionInput(BaseModel):
    id_museum: int
    name: str
    start_date: datetime
    end_date: datetime

class ExhibitionOutput(BaseModel):
    id: int
    id_museum: int
    name: str
    start_date: datetime
    end_date: datetime