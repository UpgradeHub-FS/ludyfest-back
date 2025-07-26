from BBDD.config import get_conexion
from fastapi import HTTPException
from models.user_model import User
import aiomysql
from core.security import hash_password, verify_password

    
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

async def update_by_id(user_id: int, user: User):
    if user_id != user.id:
        raise HTTPException(status_code=400, detail='El ID del usuario no coincide con el especificado en la ruta')
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            user_actual = await get_user_id(user_id)

            # Comparar la contraseña enviada con la actual
            if verify_password(user.password, user_actual['password']):
                nueva_password = user_actual['password']  # Si no se mofifica la contraseña se deja la que estaba almacenada en la base de datos
            else:
                nueva_password = hash_password(user.password)  # Si cambió, se hashea

            # Actualizar los datos
            await cursor.execute("""
                UPDATE ludyfest.users 
                SET name=%s, email=%s, password=%s, rol=%s 
                WHERE id=%s
            """, (
                user.name,
                user.email,
                nueva_password,
                user.rol,
                user_id
            ))
            await conn.commit()

            # Devolver el usuario actualizado
            user_actualizado = await get_user_id(user_id)
            
            return {
                "success": True,
                "message": "Usuario actualizado correctamente",
                "user": user_actualizado 
                }
        
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close()

       