from BBDD.config import get_conexion
from fastapi import HTTPException
from models.user_model import User, UserCreate
import aiomysql





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
            return {'msg': f'El usuario ha sido creado exitosamente', 'status': True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close()