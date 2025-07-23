from pydantic import BaseModel, EmailStr






class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
    rol: str
    
    
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    rol: str