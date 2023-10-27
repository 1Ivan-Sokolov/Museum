from fastapi import APIRouter
from src.museum.models import MuseumInput, MuseumOutput
from src.museum.resolvers import add_museum, get_museum, delete_current_museum, uppdate_museum

router = APIRouter()

@router.get('/{museum}')
def get_museum_router(museum_id: int):
    return get_museum(museum_id)

@router.post('/')
def add_museum_router(new_exhibition: MuseumInput):
    return add_museum(new_exhibition)

@router.put('/{museum_id}')
def update_museum_router(museum_id: int, new_museum: MuseumInput):
    return uppdate_museum(museum_id,new_museum)

@router.delete('/{museum_id}')
def delete_current_museum_router(museum_id: int):
    return delete_current_museum(museum_id)