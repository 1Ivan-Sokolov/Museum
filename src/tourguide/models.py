from pydantic import BaseModel

class TourguideInput(BaseModel):
    id_museum: int
    name: str


class TourguideOutput(BaseModel):
    id: int
    id_museum: int
    name: str

