from fastapi import APIRouter
from src.visitor.models import VisitorInput, VisitorOutput
from src.visitor.resolvers import add_visitor, get_visitor, delete_current_visitor, update_visitor


router = APIRouter()

@router.get('/{visitor}')
def get_visitor(id: int):
    return get_visitor()

@router.post('/{visitor_id}')
def add_visitor(new_visitor: VisitorInput):
    return add_visitor()

@router.put('/{visitor_id}')
def update_visitor(visitor_id: int, new_visitor: VisitorInput):
    return update_visitor()

@router.delete('/{visitor_id}')
def delete_current_visitor(visitor_id: int):
    return delete_current_visitor()