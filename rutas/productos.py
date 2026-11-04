from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencias import obtener_sesion, requiere_administrador
from esquemas import ProductoRespuesta, ProductoActualizar, ProductoCrear, ActualizarStock
from servicios.productos import listar_productos_servicios, obtener_producto_servicio, registrar_producto_servicio, actualizar_producto_servicio, eliminar_producto_servicio, actualizar_stock_servicio
from dependencias import obtener_sesion, obtener_usuario_actual


router = APIRouter(prefix="/productos",tags=["Productos"],dependencies=[Depends(obtener_usuario_actual)])


@router.get("/", response_model=list[ProductoRespuesta])
def listar_productos(sesion: Session = Depends(obtener_sesion)):

    productos = listar_productos_servicios(sesion)

    return productos



@router.get("/{producto_id}", response_model=ProductoRespuesta)
def obtener_producto(producto_id : int, sesion: Session = Depends(obtener_sesion)):

    producto = obtener_producto_servicio(producto_id, sesion)

    if producto:
        return producto
    else:
        raise HTTPException(status_code=404, detail="Producto no existe")



@router.post("/", status_code=201, response_model=ProductoRespuesta, dependencies=[Depends(requiere_administrador)])
def registrar_producto(datos: ProductoCrear, sesion: Session = Depends(obtener_sesion)):

    try:
        producto = registrar_producto_servicio(datos, sesion)

        return producto

    except Exception as error:
        raise HTTPException(status_code=500, detail="Producto no registrado") from error



@router.put("/{producto_id}", response_model=ProductoRespuesta, dependencies=[Depends(requiere_administrador)])
def actualizar_producto(producto_id:int, datos:ProductoActualizar, sesion: Session = Depends(obtener_sesion)):
    
    try:
        producto = actualizar_producto_servicio(producto_id, datos, sesion)

    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(status_code=500, detail="Producto no actualizado") from error

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    return producto
    


@router.delete("/{producto_id}", status_code=204, dependencies=[Depends(requiere_administrador)])
def eliminar_producto(producto_id:int, sesion: Session = Depends(obtener_sesion)):

    try:
        producto = eliminar_producto_servicio(producto_id, sesion)
    
    except Exception as error:
        raise HTTPException(status_code=500, detail="Producto no se pudo eliminar") from error

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return None 



@router.patch("/{producto_id}", dependencies=[Depends(requiere_administrador)], response_model=ProductoRespuesta)
def actualizar_stock(producto_id:int, datos:ActualizarStock, sesion: Session = Depends(obtener_sesion)):

    try:
        producto = actualizar_stock_servicio(producto_id, datos, sesion)

    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(status_code=500, detail="Stock no actualizado") from error

    if not producto:
        raise HTTPException(status_code=404, detail="producto no encontrado")

    return producto