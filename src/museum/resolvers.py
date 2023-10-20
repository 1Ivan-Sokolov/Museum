from src.database.database import base_manager
from src.museum.models import MuseumInput, MuseumOutput


def get_museum(id: int):
    result = base_manager.execute('SELECT *FROM museum WHERE id=? ', args=(id,))
    if not result:
        return None
    museum = result['data']
    museum_output = MuseumOutput(id=museum[0], name=museum[1], address=museum[2] )
    return museum_output


def add_museum(new_museum: MuseumInput):
    museum = base_manager.execute('INSERT INTO museum(name, address)'
                                 'VALUES (?, ?)',
                               (new_museum.name, new_museum.address))

def uppdate_museum(museum_id: int, museum: MuseumInput):
    museum = base_manager.execute('UPDATE museum SET name = ?, address=? WHERE id=?',
                                  args=(museum.name,museum.address,museum_id, ))

def delete_current_museum(museum_id: int):
    res = base_manager.execute("DELETE FROM groups WHERE id = ?",
                               args=(museum_id,))


