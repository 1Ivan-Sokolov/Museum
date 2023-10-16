from fastapi import APIRouter
from src.gallery.models import GalleryInput, GalleryOutput
from src.gallery.resolvers import add_gallery, get_gallery, delete_current_gallery, update_gallery

router = APIRouter()

@router.get('/{gallery}')
def get_gallery(id: int):
    return ()

@router.post('/{gallery}')
def add_gallery(new_gallery: GalleryInput):
    return add_gallery()

@router.put('/{gallery_id}')
def update_gallery(gallery_id: int, new_gallery: GalleryInput):
    return update_gallery()

@router.delete('/{gallery_id}')
def delete_current_gallery(gallery_id: int):
    return delete_current_gallery()