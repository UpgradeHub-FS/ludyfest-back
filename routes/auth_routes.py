from fastapi import APIRouter


router = APIRouter()

@router.get("/login")
def llamar():
    return {'Hola MUndo'}
