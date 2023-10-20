from fastapi import APIRouter
from src.visitor.models import VisitorInput, VisitorOutput
from src.visitor.resolvers import add_visitor, get_visitor, delete_current_visitor, update_visitor


router = APIRouter()

@router.get('/{visitor}')
def get_visitor_router(id: int):
    return get_visitor(id)

@router.post('/{visitor_id}')
def add_visitor_router(new_visitor: VisitorInput):
    return add_visitor(new_visitor)

@router.put('/{visitor_id}')
def update_visitor_router(visitor_id: int, new_visitor: VisitorInput):
    return update_visitor(visitor_id,new_visitor)

@router.delete('/{visitor_id}')
def delete_current_visitor_router(visitor_id: int):
    return delete_current_visitor(visitor_id)