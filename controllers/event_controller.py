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
            return Event(**result)  
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







async def update_event_id(event_id: int, event: Event):
    if event_id != event.id:
        raise HTTPException(status_code=400, detail="No coinciden los IDs")

    event_existente = await get_event_by_id(event_id)
    if not event_existente:
        raise HTTPException(status_code=404, detail="Evento no encontrado")

    conn = await get_conexion()
    try:
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("""
                UPDATE ludyfest.events 
                SET title=%s, description=%s, date=%s, price=%s, capacity=%s, 
                    address=%s, latitude=%s, longitude=%s, image=%s, status=%s, 
                    users_id=%s, categories_id=%s 
                WHERE id=%s
            """, (
                event.title,
                event.description,
                event.date,
                event.price,
                event.capacity,
                event.address,
                event.latitude,
                event.longitude,
                event.image,
                event.status,
                event.users_id,       
                event.categories_id,
                event_id
            ))
            await conn.commit()

            event_update = await get_event_by_id(event_id)
            return {
                "success": True,
                "message": "Evento actualizado correctamente",
                "event": event_update
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    
    finally:
            conn.close()







# BORRAR EVENTO
async def delete_event_by_id(event_id: int):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            event = await get_event_by_id(event_id)
            if not event:
                raise HTTPException(
                    status_code=404, detail='No existe el evento')
     

            await cursor.execute("DELETE FROM register_to_event WHERE events_id = %s", (event_id,))
            await cursor.execute("DELETE FROM events WHERE id = %s", (event_id,))


            await conn.commit()
            return {
                "msg": f"El evento {event_id} ha sido borrado",
                "status": True
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
            conn.close()