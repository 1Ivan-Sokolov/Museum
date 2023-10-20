from fastapi import APIRouter
from src.exhibition.models import ExhibitionInput, ExhibitionOutput
from src.exhibition.resolvers import add_exhibition, get_exhibition, delete_current_exhibition, update_exhibition

router = APIRouter()

@router.get('/{exhibition}')
def get_exhibition(id: int):
    return ()

@router.post('/{exhibition}')
def add_exhibition_router(new_exhibition: ExhibitionInput):
    return add_exhibition(new_exhibition)

@router.put('/{exhibition_id}')
def update_exhibition_router(exhibition_id: int, new_ticket: ExhibitionInput):
    return update_exhibition(exhibition_id,new_ticket)

@router.delete('/{exhibition_id}')
def delete_current_exhibition_router(exhibition_id: int):
    return delete_current_exhibition(exhibition_id)