from BBDD.config import get_conexion
from fastapi import HTTPException
from models.event_model import Event
import aiomysql

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
    