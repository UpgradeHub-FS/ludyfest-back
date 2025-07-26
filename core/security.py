# Se necesitran las librerías de python python-jose => criptografia para el token, passlib => bcrypt para el hasheo
# pip install "python-jose[cryptography]"
# pip install "passlib[bcrypt]"

#Importaciones
import os  # os la necesitamos para cargar variables de entorno
from passlib.context import CryptContext # para hashear contraseñas
from dotenv import load_dotenv

# Se cargan las variables de entorno
load_dotenv() 

# Se configura bcrypt para poderlo usar en este fichero. Para ello tengo que generar lo que se llama contexto
pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password) # Hashea una contraseña usando bcrypt

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password) # Verifica que una contraseña en texto plano coincida con su hash.