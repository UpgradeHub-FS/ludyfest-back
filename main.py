from fastapi import FastAPI
from routes import user_routes
from routes import auth_routes

app = FastAPI()

#Creo acceso a la ruta user
app.include_router(user_routes.router,
                   prefix="/users",
                   tags=["Users"])
#Creación ruta login
app.include_router(auth_routes.router, 
                   prefix="/auth", 
                   tags=['Auth'])
