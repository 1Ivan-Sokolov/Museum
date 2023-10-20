from src.database.database import base_manager
from src.exhibition.models import ExhibitionInput, ExhibitionOutput

def get_exhibition(id: int):
    result = base_manager.execute('SELECT * FROM exhibition WHERE id=? ', args=(id, ))
    if not result:
        return None
    exhibition = result['data']
    exhibition_output = ExhibitionOutput(id=exhibition[0], id_museum=exhibition[1], name=exhibition[2], star_date=exhibition[3], end_date=exhibition[4])
    return exhibition_output

def add_exhibition(new_exhibition: ExhibitionInput):
    exhibition = base_manager.execute('INSERT INTO exhibition(id_museum, name, start_date, end_date)'
                                      'VALUES(?, ?, ?, ? )', args=(new_exhibition.id_museum, new_exhibition.name, new_exhibition.start_date, new_exhibition.end_date))


def update_exhibition(exhibition_id: int, new_exhibition: ExhibitionInput):
    exhibition = base_manager.execute('UPDATE exhibition SET id_museum=?, name=?, start_date=?, end_date=? WHERE id=? ', args=(new_exhibition.id_museum, new_exhibition.name, new_exhibition.start_date, new_exhibition.end_date, exhibition_id))

def delete_current_exhibition(exhibition_id: int):
    exhibition = base_manager.execute('DELETE FROM exhibition WHERE id=?', args=(exhibition_id,))