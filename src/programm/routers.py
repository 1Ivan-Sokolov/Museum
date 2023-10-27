from fastapi import APIRouter
from src.programm.models import ProgrammInput, ProgrammOutput
from src.programm.resolvers import add_programm, get_programm, delete_current_programm, update_programm

router = APIRouter()

@router.get('/{programm}')
def get_programm_router(programm_id: int):
    return get_programm(programm_id)

@router.post('/')
def add_programm_router(new_programm: ProgrammInput):
    return add_programm(new_programm)

@router.put('/{programm_id}')
def update_programm_router(programm_id: int, new_programm: ProgrammInput):
    return update_programm(programm_id,new_programm)

@router.delete('/{programm_id}')
def delete_current_programm_router(programm_id: int):
    return delete_current_programm(programm_id)