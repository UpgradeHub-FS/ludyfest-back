from fastapi import APIRouter
from models.user_model import UserCreate, UserLogin
from controllers import auth_controllers


router = APIRouter()

#Creación de login mediante Post 
@router.post("/login", status_code=200)
async def login(user_login: UserLogin):
    return await auth_controllers.login(user_login)

#Creación de usuario mediante POST
@router.post('/register', status_code=201)
async def user_create(user: UserCreate):
    return await auth_controllers.user_create(user)
