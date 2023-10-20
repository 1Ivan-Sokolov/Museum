from fastapi import APIRouter
from src.artwork.models import ArtworkInput,ArtworkOutput
from src.artwork.resolvers import add_artwork, get_artwork, delete_current_artwork, update_artwork

router = APIRouter()

@router.get('/{artwork}')
def get_artwork_router(id: int):
    return get_artwork(id)

@router.post('/{artwork}')
def add_artwork_router(new_artwork: ArtworkInput):
    return add_artwork(new_artwork)

@router.put('/{artwork_id}')
def update_artwork_router(artwork_id: int, new_artwork: ArtworkInput):
    return update_artwork(artwork_id, new_artwork)

@router.delete('/{artwork}')
def delete_current_artwork_router(ticket_id: int):
    return delete_current_artwork(ticket_id)