from src.database.database import base_manager
from src.artwork.models import ArtworkInput, ArtworkOutput


def get_artwork(id: int):
    result = base_manager.execute('SELECT * FROM artwork WHERE id=?', args=(id, ))
    if not result:
        return None
    artwork = result['data']
    artwork_output = ArtworkOutput(id=artwork[0], id_exhibition=artwork[1], title=artwork[2], year=artwork[3], artist=artwork[4], mediom=artwork[5], description=artwork[6])
    return artwork_output


def add_artwork(new_artwork: ArtworkInput):
    artwork = base_manager.execute("INSERT INTO artwork(title, year, artist, mediom, description, id_exhibition) " 
                               "VALUES (?, ?, ?, ?, ?, ?) ",
                                (new_artwork.title, new_artwork.year, new_artwork.artist, new_artwork.mediom, new_artwork.description, new_artwork.id_exhibition))

def update_artwork(artwork_id: int, new_artwork: ArtworkInput):
    artwork = base_manager.execute('UPDATE artwork SET title=?, year=?, artist=?, mediom=?, description=?, id_exhibition=? WHERE id=?',
                                    (new_artwork.title, new_artwork.year, new_artwork.artist, new_artwork.mediom, new_artwork.description,new_artwork.id_exhibition, artwork_id))


def delete_current_artwork(id: int):
    artwork = base_manager.execute('DELETE FROM artwork WHERE id=?', args=(id,))
