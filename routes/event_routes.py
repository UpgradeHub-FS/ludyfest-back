
from fastapi import APIRouter
from controllers import event_controller
from models.event_model import Event

router = APIRouter()

@router.get('/{event_id}', status_code=200)
async def get_event_by_id(event_id: int):
    return await event_controller.get_event_by_id(event_id)
