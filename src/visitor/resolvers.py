from src.database.database import base_manager
from src.visitor.models import VisitorInput, VisitorOutput

def get_visitor(id: int):
    visitor = base_manager.execute('SELECT * FROM visitor WHERE id=?', args=(id,))['data'][0]
    visitor_output = VisitorOutput(id=visitor[0], name=visitor[1], surname=visitor[2], email=visitor[3], contacts=visitor[4])
    return visitor_output

def add_visitor(new_visitor: VisitorInput):
    visitor = base_manager.execute('INSERT INTO visitor(name, surname, email, contacts)'
                                   'VALUES (?, ?, ?, ?)', args=(new_visitor.name, new_visitor.surname, new_visitor.email, new_visitor.contacts))

def update_visitor(visitor_id: int, new_visitor: VisitorInput):
    visitor = base_manager.execute('UPDATE visitor SET name=?, surname=?, email=?, contacts=?  WHERE id=?', args=(new_visitor.name, new_visitor.surname, new_visitor.email, new_visitor.contacts, visitor_id))

def delete_current_visitor(visitor_id: int):
    visitor = base_manager.execute('DELETE FROM visitor WHERE id=? ', args=(visitor_id,))