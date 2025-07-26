from BBDD.config import get_conexion
from fastapi import HTTPException
from models.user_model import User, UserCreate
import aiomysql




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
            return {'msg': f'El usuario ha sido creado exitosamente', 'status': True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close()
        
        
#Funcion ver todos los usuarios

async def get_users_list():
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute('SELECT * FROM ludyfest.users')
            data = await cursor.fetchall()
            
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    
    finally:
        conn.close()
        
#Funcion buscar user por id

async def get_user_id(user_id: int):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("SELECT * FROM ludyfest.users WHERE id=%s", (user_id,))
            user = await cursor.fetchone()
            if not user:
                raise HTTPException(
                    status_code=404, detail='Usuario no encontrado')
            else:
                return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close()
        
#Funcion borrar user por id

async def delete_by_id(user_id: int):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            # verificar el usuario existe.
            user = await get_user_id(user_id)
            if not user:
                raise HTTPException(
                    status_code=404, detail='Usuario no existe')
            # Eliminar el usuario
            await cursor.execute('DELETE FROM ludyfest.users WHERE id=%s', (user_id,))
            await conn.commit()
            return {"msg": f"Usuario con id {user_id} eliminado correctamente", "status": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close()