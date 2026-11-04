from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta, timezone
from configuracion import SECRET_KEY

password_hash = PasswordHash.recommended()

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def generar_hash(password: str):
    return password_hash.hash(password)


def verificar_password(password: str, hash_almacenado: str):
    return password_hash.verify(password, hash_almacenado)


def crear_token(usuario_id:int):

    hora_actual = datetime.now(timezone.utc)

    expiracion = hora_actual + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    datos = {"sub": str(usuario_id), "exp":expiracion}

    token = jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)

    return token
