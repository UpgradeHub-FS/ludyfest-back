from fastapi import APIRouter
from controllers import user_controller
from models.user_model import User, UserCreate



router = APIRouter()



#Creacion de get_users_list mediante POST
@router.get('/', status_code=200)
async def get_all():
    return await user_controller.get_users_list()

#Creacion de get_user_id mediante GET
@router.get('/{user_id}', status_code=200)
async def get_user_id(user_id: int):
    return await user_controller.get_user_id(user_id)

#Creacion de delete_by_id mediante DELETE
@router.delete('/{user_id}', status_code=200)
async def delete_by_id(user_id: int):
    return await user_controller.delete_by_id(user_id)