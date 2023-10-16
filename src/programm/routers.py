from fastapi import APIRouter
from src.programm.models import ProgrammInput, ProgrammOutput
from src.programm.resolvers import add_programm, get_programm, delete_current_programm, update_programm

router = APIRouter()

@router.get('/{programm}')
def get_programm(id: int):
    return get_programm()

@router.post('/{programm}')
def add_programm(new_programm: ProgrammInput):
    return add_programm()

@router.put('/{programm_id}')
def update_programm(programm_id: int, new_programm: ProgrammInput):
    return update_programm()

@router.delete('/{programm_id}')
def delete_current_programm(programm_id: int):
    return delete_current_programm()