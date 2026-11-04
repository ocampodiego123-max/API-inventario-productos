from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from dependencias import obtener_sesion, requiere_administrador, obtener_usuario_actual
from esquemas import CantidadCompra, RespuestaCompra
from servicios.compras import registrar_compra_servicio, consultar_compras_por_producto_servicio


router = APIRouter(prefix="/compras",tags=["Compras"],dependencies=[Depends(obtener_usuario_actual)])


@router.post("/{producto_id}",status_code=201, response_model=RespuestaCompra, dependencies=[Depends(requiere_administrador)])
def registrar_compra(producto_id:int, datos: CantidadCompra, sesion: Session = Depends(obtener_sesion)):

    try:
        compra = registrar_compra_servicio(producto_id, datos, sesion)

    except HTTPException:
        raise

    if compra is False:
        raise HTTPException(status_code=409, detail="No hay stock suficiente")        

    if compra is None:
        raise HTTPException(status_code=404, detail="producto no encontrado")

    return compra


@router.get("/{producto_id}")
def consultar_compras_por_producto(producto_id:int, sesion: Session = Depends(obtener_sesion)):

    try:
        consulta_compra = consultar_compras_por_producto_servicio(producto_id, sesion)

    except Exception as error:
        raise HTTPException(status_code=500, detail="No se pudo hacer la consulta") from error

    if consulta_compra is None:
        raise HTTPException(status_code=404, detail="No existe el producto")

    if not consulta_compra:
        return []

    return consulta_compra