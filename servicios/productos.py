from sqlalchemy import select
from sqlalchemy.orm import Session
from modelos import Producto


def listar_productos_servicios(sesion: Session):

    productos = sesion.scalars(select(Producto)).all()

    return productos


def obtener_producto_servicio(producto_id: int, sesion: Session):

    producto = sesion.scalars(select(Producto).where(Producto.id == producto_id)).first()

    return producto


def registrar_producto_servicio(datos, sesion: Session):

    try:
        producto = Producto(nombre=datos.nombre, stock=datos.stock, precio=datos.precio)
        
        sesion.add(producto)
        sesion.commit()
        sesion.refresh(producto)

        return producto
    
    except Exception:
        sesion.rollback()
        raise


def actualizar_producto_servicio(producto_id:int, datos, sesion: Session):

    try:
        producto = sesion.scalars(select(Producto).where(Producto.id == producto_id)).first()

        if not producto:
            return None

        producto.nombre = datos.nombre
        producto.stock = datos.stock
        producto.precio = datos.precio

        sesion.commit()
        sesion.refresh(producto)

        return producto

    except Exception:
        sesion.rollback()
        raise


def eliminar_producto_servicio(producto_id:int, sesion: Session):

    try:
        producto = sesion.scalars(select(Producto).where(Producto.id == producto_id)).first()

        if not producto:
            return False
            
        sesion.delete(producto)
        sesion.commit()

        return True

    except Exception:
        sesion.rollback()
        raise


def actualizar_stock_servicio(producto_id:int, datos, sesion:Session):

    try:
        producto = sesion.scalars(select(Producto).where(Producto.id == producto_id)).first()
    
        if not producto:
            return None

        if datos.nuevo_stock > 0:
            producto.stock += datos.nuevo_stock
            sesion.commit()
            sesion.refresh(producto)

            return producto

    except Exception:
        sesion.rollback()
        raise