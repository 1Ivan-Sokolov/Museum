from fastapi import APIRouter

from src.ticket.models import TicketInput, TicketOutput
from src.ticket.resolvers import add_ticket, get_ticket, delete_current_ticket, update_ticket

router = APIRouter()

@router.get('/{ticket}')
def get_ticket(id: int):
    return get_ticket(id=id)

@router.post('/{ticket_buy}')
def add_ticket(new_ticket: TicketInput):
    return add_ticket()

@router.put('/{ticket_id}')
def update_ticket(ticket_id: int, new_ticket: TicketInput):
    return update_ticket()

@router.delete('/{ticket_id}')
def delete_current_ticket(ticket_id: int):
    return delete_current_ticket()