from fastapi import APIRouter
from controllers import event_controller

router = APIRouter()

#obtener todos los eventos con GET (usa la ruta del main.py)
#http://localhost:8000/eventos/
@router.get('/', status_code=200)
async def get_all():
    return await event_controller.get_event_list()

