from fastapi import APIRouter, Depends, HTTPException
from esquemas import UsuarioCrear, UsuarioRespuesta, TokenRespuesta
from dependencias import obtener_sesion
from servicios.usuarios import registrar_usuario, autenticar_usuario
from sqlalchemy.orm import Session
from seguridad import crear_token
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()

@router.post("/registro", status_code=201, response_model=UsuarioRespuesta)
def registro_usuario(datos:UsuarioCrear, sesion: Session = Depends(obtener_sesion)):

    usuario_nuevo = registrar_usuario(datos.usuario, datos.password, sesion)

    if not usuario_nuevo:
        raise HTTPException(status_code=409, detail="Usuario ya existe")

    return usuario_nuevo


@router.post("/login", response_model=TokenRespuesta)
def login_usuario(datos: OAuth2PasswordRequestForm = Depends(), sesion: Session= Depends(obtener_sesion)):

    autenticado = autenticar_usuario(datos.username, datos.password, sesion)

    if not autenticado:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    token = crear_token(autenticado.id)

    return {"access_token": token, "token_type":"bearer"}