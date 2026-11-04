from modelos import Producto, Compra
from sqlalchemy import select
from sqlalchemy.orm import Session


def registrar_compra_servicio(producto_id:int, datos, sesion: Session):

    try: 
        producto = sesion.scalars(select(Producto).where(Producto.id == producto_id).with_for_update()).first()

        if producto:
            if producto.stock >= datos.cantidad:
                producto.stock -= datos.cantidad
                compra = Compra(producto_id=producto.id, cantidad=datos.cantidad, total=datos.cantidad*producto.precio)
                sesion.add(compra)
                sesion.commit()
                sesion.refresh(compra)
                return compra
            else:
                sesion.rollback()
                return False
        else:
            sesion.rollback()
            return None

    except Exception:
        sesion.rollback()
        raise



def consultar_compras_por_producto_servicio(producto_id:int, sesion: Session):

    try:
        producto = sesion.get(Producto, producto_id)

        if producto is None:
            return None

        if not producto.compras:
            return []
            
        return producto.compras

    except Exception:
        sesion.rollback()
        raise