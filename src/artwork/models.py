from pydantic import BaseModel
from datetime import date

class ArtworkInput(BaseModel):
    id_exhibition: int
    title: str
    year: date
    artist: str
    mediom: str
    description: str

class ArtworkOutput(BaseModel):
    id: int
    id_exhibition: int
    title: str
    year: date
    artist: str
    mediom: str
    description: str
