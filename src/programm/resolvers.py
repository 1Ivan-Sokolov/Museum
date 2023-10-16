from src.database.database import base_manager
from src.programm.models import ProgrammInput, ProgrammOutput

def get_programm(id: int):
    programm = base_manager.execute('SELECT * FROM programm WHERE id=?', args=(id,))['data'][0]
    programm_output = ProgrammOutput(id=programm[0], id_museum=programm[1], name=programm[2], date=programm[3], description=programm[4])
    return programm_output

def add_programm(new_programm: ProgrammInput):
    programm = base_manager.execute('INSERT INTO programm (id_museum, name, date, description)'
                                   'VALUES (?, ?, ?, ?)', args=(new_programm.id_museum, new_programm.name, new_programm.date, new_programm.description))

def update_programm(programm_id: int, new_programm: ProgrammInput):
    programm = base_manager.execute('UPDATE programm SET id_museum=?, name=?, date=?,description=?  WHERE id=?', args=( new_programm.id_museum, new_programm.name, new_programm.date, new_programm.description, programm_id))

def delete_current_programm(programm_id: int):
    programm = base_manager.execute('DELETE FROM programm WHERE id=? ', args=(programm_id,))