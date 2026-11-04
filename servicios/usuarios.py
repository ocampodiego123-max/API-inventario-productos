from sqlalchemy import select
from sqlalchemy.orm import Session

from modelos import Usuario
from seguridad import generar_hash, verificar_password



def registrar_usuario(usuario: str, password:str, sesion: Session):

    usuario_existente = sesion.scalars(select(Usuario).where(Usuario.usuario == usuario)).first()

    if usuario_existente:
        return None

    try:
        password = generar_hash(password)

        nuevo_usuario = Usuario(usuario=usuario, password_hash=password, rol='usuario')

        sesion.add(nuevo_usuario)
        sesion.commit()
        sesion.refresh(nuevo_usuario)

        return nuevo_usuario

    except Exception:
        sesion.rollback()
        raise


def autenticar_usuario(usuario:str, password:str, sesion:Session):

    usuario_buscado = sesion.scalars(select(Usuario).where(Usuario.usuario==usuario)).first()

    if not usuario_buscado:
        return None

    if not verificar_password(password, usuario_buscado.password_hash):
        return None

    return usuario_buscado   