from src.database.database import base_manager
from src.tourguide.models import TourguideInput, TourguideOutput


def get_tourguide(id: int):
    tourguide = base_manager.execute('SELECT * FROM tourguide WHERE id=? ', args=(id,))['data'][0]
    tourguide_output = TourguideOutput(id=tourguide[0],id_museum=tourguide[1], name=tourguide[2])
    return tourguide_output


def add_tourguide(new_tourguide: TourguideInput):
    tourguide = base_manager.execute('INSERT INTO tourguide(id_museum, name)'
                                 'VALUES (?, ?)',
                               (new_tourguide.id_museum, new_tourguide.name))

def update_tourguide(tourguide_id: int,new_tourguide: TourguideInput):
    tourguide = base_manager.execute('UPDATE tourguide SET id_museum = ?, name=? WHERE id=?',
                                  args=(new_tourguide.id_museum, new_tourguide.name, tourguide_id))

def delete_current_tourguide(tourguide_id: int):
    tourguide = base_manager.execute("DELETE FROM tourguide WHERE id = ?",
                               args=(tourguide_id,))

