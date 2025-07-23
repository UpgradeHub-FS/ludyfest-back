from fastapi import APIRouter
from controllers import user_controller
from models.user_model import User, UserCreate



router = APIRouter()


@router.post('/', status_code=201)
async def user_create(user: UserCreate):
    return await user_controller.user_create(user)