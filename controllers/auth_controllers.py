from fastapi import HTTPException
from BBDD.config import get_conexion
from models.user_model import UserCreate, UserLogin
import aiomysql




async def login(user_login: UserLogin):

    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("SELECT * FROM ludyfest.users WHERE email =%s", (user_login.email,))
            user = await cursor.fetchone()

            if not user or user['password'] != user_login.password:
                raise HTTPException(
                    status_code=404, detail='Usuario o password incorrecto')

            return {
                "success": True,
                "message": "Usuario logueado correctamente",
                "user": user  # esto es el usuario que sacaste de la BD
                }


    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error:{str(e)}")
    finally:
        conn.close()


#Funcion para crear un usuario
async def user_create(user: UserCreate):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("INSERT INTO ludyfest.users (name, email, password, rol) VALUES (%s,%s,%s,%s)", (
                user.name,
                user.email,
                user.password,
                user.rol
            ))
            await conn.commit()
            return {
                "success": True,
                "message": "Usuario creado correctamente",
                "user": user  # esto es el usuario que sacaste de la BD
                }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close()