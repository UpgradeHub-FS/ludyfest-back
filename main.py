from fastapi import FastAPI
from routes import event_routes

app = FastAPI()
#crear la ruta para los eventos
app.include_router(event_routes.router,
                   prefix="/eventos",
                   tags=["Eventos"])

@app.get("/")
def root():
    return {"message": "Servidor funcionando"}
