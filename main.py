from fastapi import FastAPI
from routes import user_routes

app = FastAPI()

#Creo acceso a la ruta user
app.include_router(user_routes.router,
                   prefix="/users",
                   tags=["Users"])