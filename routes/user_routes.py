from fastapi import APIRouter
from controllers import user_controller
from models.user_model import User, UserCreate



router = APIRouter()

#Creacion de usuario mediante POST
@router.post('/register', status_code=201)
async def user_create(user: UserCreate):
    return await user_controller.user_create(user)