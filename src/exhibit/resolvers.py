from src.database.database import base_manager
from src.exhibit.models import ExhibitInput, ExhibitOutput

def get_exhibit(id: int):
    result = base_manager.execute('SELECT * FROM exhibit WHERE id=?', args=(id,))
    if not result:
        return None
    exhibit = result['data']
    exhibit_output = ExhibitOutput(id=exhibit[0], id_exhibition=exhibit[1], name=exhibit[2], category=exhibit[3], year_of_creation=exhibit[4], author=exhibit[5])
    return exhibit_output

def add_exhibit(new_exhibit: ExhibitInput):
    exhibit = base_manager.execute('INSERT INTO exhibit(id_exhibition, name, category, year_of_creation, author)'
                                   'VALUES (?, ?, ?, ?, ?)', args=(new_exhibit.id_exhibition, new_exhibit.name, new_exhibit.category, new_exhibit.year_of_creation, new_exhibit.author))

def update_exhibit(exhibit_id: int, new_exhibit:  ExhibitInput):
    exhibit = base_manager.execute('UPDATE exhibit SET id_exhibition=?, name=?, category=?, year_of_creation=?, author=? WHERE id=?', args=(new_exhibit.id_exhibition, new_exhibit.name, new_exhibit.category, new_exhibit.year_of_creation, new_exhibit.author, exhibit_id))

def delete_current_exhibit(exhibit_id: int):
    exhibit = base_manager.execute('DELETE FROM exhibit WHERE id=? ', args=(exhibit_id,))