from src.database.database import base_manager
from src.gallery.models import GalleryInput, GalleryOutput

def get_gallery(id: int):
    gallery = base_manager.execute('SELECT * FROM gallery WHERE id=?', args=(id,))['data'][0]
    gallery_output = GalleryOutput(id=gallery[0], id_museum=gallery[1], name=gallery[2])
    return gallery_output

def add_gallery(new_gallery: GalleryInput):
    gallery = base_manager.execute('INSERT INTO gallery(id_museum, name)'
                                   'VALUES (?, ?)', args=(new_gallery.id_museum, new_gallery.name))

def update_gallery(gallery_id: int, new_gallery: GalleryInput):
    gallery = base_manager.execute('UPDATE gallery SET id_museum=?, name=? WHERE id=?', args=(new_gallery.id_museum, new_gallery.name, gallery_id))

def delete_current_gallery(gallery_id: int):
    gallery = base_manager.execute('DELETE FROM gallery WHERE id=? ', args=(gallery_id,))