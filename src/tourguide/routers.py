from fastapi import APIRouter
from src.tourguide.models import TourguideInput,TourguideOutput
from src.tourguide.resolvers import add_tourguide, get_tourguide, delete_current_tourguide, update_tourguide

router = APIRouter()

@router.get('/{tourguide}')
def get_tourguide(id: int):
    return get_tourguide()

@router.post('/{tourguide}')
def add_tourguide(new_tourguide: TourguideInput):
    return add_tourguide()

@router.put('/{tourguide_id}')
def update_tourguide(tourguide_id: int, new_tourguide: TourguideInput):
    return update_tourguide()

@router.delete('/{tourguide_id}')
def delete_current_tourguide(tourguide_id: int):
    return delete_current_tourguide()