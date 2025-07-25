from fastapi import HTTPException
from models.event_model import Event
from BBDD.config import get_conexion
import aiomysql



#get by_id para obtener un evento
async def get_event_by_id(event_id: int):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("SELECT * FROM ludyfest.events WHERE id=%s", (event_id,))
            result = await cursor.fetchone() 
            if not result:
                raise HTTPException(status_code=404, detail="Evento no encontrado")
            return Event(result)  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
    finally:
        conn.close()

#GET para obtener todos los eventos
async def get_event_list():
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor: 
            await cursor.execute('SELECT * FROM ludyfest.events')
            data = await cursor.fetchall()
            return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
            conn.close()
#GET para obtener todos los eventos para admin
async def get_event_list_admin():
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor: 
            await cursor.execute('SELECT * FROM ludyfest.events')
            data = await cursor.fetchall()
            return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
            conn.close()
    
