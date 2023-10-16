from fastapi import APIRouter
from src.museum.models import MuseumInput, MuseumOutput
from src.museum.resolvers import add_museum, get_museum, delete_current_museum, uppdate_museum

router = APIRouter()

@router.get('/{museum}')
def get_museum(id: int):
    return get_museum()

@router.post('/{museum}')
def add_museum(new_exhibition: MuseumInput):
    return add_museum()

@router.put('/{museum_id}')
def update_museum(museum_id: int, new_museum: MuseumInput):
    return update_museum()

@router.delete('/{museum_id}')
def delete_current_museum(museum_id: int):
    return delete_current_museum()