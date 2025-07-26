
from fastapi import APIRouter
from controllers import event_controller
from models.event_model import Event
from controllers.event_controller import update_event_id
router = APIRouter()

#obtener todos los eventos con GET (usa la ruta del main.py)
#http://localhost:8000/events/
@router.get('/', status_code=200)
async def get_all():
    return await event_controller.get_event_list()


#http://localhost:8000/events/{event_id}
@router.get('/{event_id}', status_code=200)
async def get_event_by_id(event_id: int):
    return await event_controller.get_event_by_id(event_id)


 
# ACTUALIZAR EVENTO
@router.put("/{event_id}")
async def update_event(event_id: int, event: Event):
    return await update_event_id(event_id, event)

# BORRAR EVENTO
@router.delete('/{event_id}', status_code=200)
async def delete_event_by_id(event_id: int):
    return await event_controller.delete_event_by_id(event_id)