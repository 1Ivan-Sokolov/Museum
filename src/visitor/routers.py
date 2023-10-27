from fastapi import APIRouter
from src.visitor.models import VisitorInput
from src.visitor.resolvers import add_visitor, get_visitor, delete_current_visitor, update_visitor, check_visitor


router = APIRouter()

@router.get('/check')
def check_exists_visitor(user: VisitorInput):
    return check_visitor(user)

@router.get('/{visitor_id}')
def get_visitor_router(visitor_id: int):
    return get_visitor(visitor_id)

@router.post('/')
def add_visitor_router(new_visitor: VisitorInput):
    return add_visitor(new_visitor)

@router.put('/{visitor_id}')
def update_visitor_router(visitor_id: int, new_visitor: VisitorInput):
    return update_visitor(visitor_id,new_visitor)

@router.delete('/{visitor_id}')
def delete_current_visitor_router(visitor_id: int):
    return delete_current_visitor(visitor_id)