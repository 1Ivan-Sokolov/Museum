from fastapi import APIRouter
from src.exhibit.models import ExhibitInput, ExhibitOutput
from src.exhibit.resolvers import add_exhibit, get_exhibit, delete_current_exhibit, update_exhibit

router = APIRouter()

@router.get('/{exhibit}')
def get_exhibit_router(exhibit_id: int):
    return get_exhibit(exhibit_id)

@router.post('/')
def add_exhibit_router(new_exhibit: ExhibitInput):
    return add_exhibit(new_exhibit)

@router.put('/{exhibit_id}')
def update_exhibit_router(exhibit_id: int, new_exhibit: ExhibitInput):
    return update_exhibit(exhibit_id,new_exhibit)

@router.delete('/{exhibit_id}')
def delete_current_exhibit_router(exhibit_id: int):
    return delete_current_exhibit(exhibit_id)