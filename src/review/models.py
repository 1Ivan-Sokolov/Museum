from pydantic import BaseModel

class ReviewInput(BaseModel):
    id_exhibition: int
    id_visitor: int
    rating: float
    comment:str

class ReviewOutput(BaseModel):
    id: int
    id_exhibition: int
    id_visitor: int
    rating: float
    comment: str