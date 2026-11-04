from base_datos import SessionLocal
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy import select
import jwt
from seguridad import ALGORITHM
from configuracion import SECRET_KEY
from modelos import Usuario


oauth2_esquema = OAuth2PasswordBearer(tokenUrl="/login")

def obtener_sesion():

    sesion = SessionLocal()

    try:
        yield sesion
    finally:
        sesion.close()
        
        

def obtener_usuario_actual(token:str = Depends(oauth2_esquema), sesion: Session = Depends(obtener_sesion)):

    try:
        datos = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        sub = int(datos["sub"])

        usuario_bd = sesion.scalars(select(Usuario).where(Usuario.id == sub)).first()

        if not usuario_bd:
            raise HTTPException(status_code=401, detail="No se pudo validar la autenticación")

        return usuario_bd

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token no válido")
    
    except (ValueError, KeyError):
        raise HTTPException(status_code=401, detail="Token no válido")



def requiere_administrador(usuario: Usuario = Depends(obtener_usuario_actual)):

    if not usuario.rol == 'administrador':
        raise HTTPException(status_code=403, detail="Usuario no autorizado")

    return usuario



    


    

    



