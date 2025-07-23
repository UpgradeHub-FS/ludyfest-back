from fastapi import HTTPException
from BBDD.config import get_conexion
from models.user_models import UserLogin
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

            return {'Usuario logado correctamente'}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error:{str(e)}")
    finally:
        conn.close()
