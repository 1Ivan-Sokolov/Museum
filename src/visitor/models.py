from pydantic import BaseModel

class VisitorInput(BaseModel):

    name: str
    surname: str
    email: str
    contacts: str

class VisitorOutput(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    contacts: str