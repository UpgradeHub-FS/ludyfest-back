from fastapi import APIRouter
from models.user_model import UserLogin
from controllers import auth_controllers


router = APIRouter()


@router.post("/login", status_code=200)
async def login(user_login: UserLogin):
    return await auth_controllers.login(user_login)
