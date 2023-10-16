from pydantic import BaseModel

class GalleryInput(BaseModel):
    id_museum: int
    name: str

class GalleryOutput(BaseModel):
    id: int
    id_museum: int
    name: str

