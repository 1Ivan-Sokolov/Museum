from pydantic import BaseModel

class MuseumInput(BaseModel):
    name: str
    address: str

class MuseumOutput(BaseModel):
    id: int
    name: str
    address: str
