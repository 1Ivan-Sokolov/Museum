from src.database.database import base_manager
from src.ticket.models import TicketInput, TicketOutput

def get_ticket(id: int):
    ticket = base_manager.execute('SELECT * FROM ticket WHERE id=?', args=(id,))['data'][0]
    ticket_output = TicketOutput(id=ticket[0], id_museum=ticket[1], id_exhibition=ticket[2], id_visitor=ticket[3], name=ticket[4], date=ticket[5], time=ticket[5], ticket_price=ticket[6])
    return ticket_output

def add_ticket(new_ticket: TicketInput):
    ticket = base_manager.execute('INSERT INTO ticket(id_museum, id_exhibition, id_visitor, name, date, time, ticket_price )'
                                   'VALUES (?, ?, ?, ?, ?, ?, ?)', args=(new_ticket.id_museum, new_ticket.id_exhibition, new_ticket.id_visitor, new_ticket.date, new_ticket.time, new_ticket.ticket_price))

def update_ticket(ticket_id: int, new_ticket: TicketInput):
    ticket = base_manager.execute('UPDATE ticket SET id_museum=?, id_exhibition=?, id_visitor=?, name=?, date=?, time=?, ticket_price=?  WHERE id=?', args=(new_ticket.id_museum, new_ticket.id_exhibition, new_ticket.id_visitor, new_ticket.date, new_ticket.time, new_ticket.ticket_price, ticket_id))

def delete_current_ticket(ticket_id: int):
    ticket = base_manager.execute('DELETE FROM ticket WHERE id=? ', args=(ticket_id,))