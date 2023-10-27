from src.database.database import base_manager
from src.visitor.models import VisitorInput, VisitorOutput

def check_visitor(login: VisitorInput):
    res = base_manager.execute("SELECT id"
                               "FROM visitor "
                               "WHERE email=? AND password=?", args=(login.email.lower(), login.password), many=False)
    print(res)
    if res['data']:
        return True
    return False


def get_visitor(id: int):
    result = base_manager.execute('SELECT * FROM visitor WHERE id=?', args=(id,))
    if not result:
        return None
    visitor = result['data']
    visitor_output = VisitorOutput(id=visitor[0], name=visitor[1], surname=visitor[2], password=visitor[3],email=visitor[4], contacts=visitor[5])
    return visitor_output

def add_visitor(new_visitor: VisitorInput):
    visitor = base_manager.execute('INSERT INTO visitor(name, surname,password, email, contacts)'
                                   'VALUES (?, ?, ?, ?, ?)', args=(new_visitor.name, new_visitor.surname, new_visitor.password, new_visitor.email, new_visitor.contacts))

def update_visitor(visitor_id: int, new_visitor: VisitorInput):
    visitor = base_manager.execute('UPDATE visitor SET name=?, surname=?, password=?, email=?, contacts=? WHERE id=?', args=(new_visitor.name, new_visitor.surname,new_visitor.password, new_visitor.email, new_visitor.contacts, visitor_id))

def delete_current_visitor(visitor_id: int):
    visitor = base_manager.execute('DELETE FROM visitor WHERE id=? ', args=(visitor_id,))