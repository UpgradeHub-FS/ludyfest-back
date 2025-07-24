from fastapi import FastAPI
from routes import user_routes,event_routes

app = FastAPI()

#Creo acceso a la ruta user
app.include_router(user_routes.router,
                   prefix="/users",
                   tags=["Users"])



app.include_router(event_routes.router, 
                   prefix="/events", 
                   tags=["Events"])