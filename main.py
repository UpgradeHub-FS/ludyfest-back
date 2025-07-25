from fastapi import FastAPI
from routes import event_routes, user_routes, auth_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
#crear la ruta para los eventos
app.include_router(event_routes.router, 
                   prefix="/events", 
                   tags=["Events"])

#Creación ruta login
app.include_router(auth_routes.router, 
                   prefix="/auth", 
                   tags=['Auth'])

#Creo acceso a la ruta user
app.include_router(user_routes.router,
                   prefix="/users",
                   tags=["Users"])

#Hago la conexión entre el back y el front
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # o [""] para pruebas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)