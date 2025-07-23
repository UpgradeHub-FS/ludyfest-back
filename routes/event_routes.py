from fastapi import APIRouter
from controllers import event_controller
router = APIRouter()

@router.get('/', status_code=200)
async def get_all():
    return await event_controller.get_event_list()