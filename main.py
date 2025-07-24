from fastapi import FastAPI
from routes import event_routes, user_routes, auth_routes

app = FastAPI()
#crear la ruta para los eventos
app.include_router(event_routes.router,
                   prefix="/eventos",
                   tags=["Eventos"])

#Creación ruta login
app.include_router(auth_routes.router, 
                   prefix="/auth", 
                   tags=['Auth'])

#Creo acceso a la ruta user
app.include_router(user_routes.router,
                   prefix="/users",
                   tags=["Users"])
