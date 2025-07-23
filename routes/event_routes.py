from fastapi import APIRouter
from controllers import event_controller
router = APIRouter()

#obtener todos los eventos con GET usando la ruta del main
@router.get('/', status_code=200)
async def get_all():
    return await event_controller.get_event_list()