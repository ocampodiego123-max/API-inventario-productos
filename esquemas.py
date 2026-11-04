from pydantic import BaseModel, ConfigDict, Field
from decimal import Decimal


class ProductoRespuesta(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str
    stock: int
    precio: Decimal


class ProductoCrear(BaseModel):

    nombre: str
    stock: int
    precio: Decimal



class ProductoActualizar(BaseModel):

    nombre: str
    stock: int
    precio: Decimal



class ActualizarStock(BaseModel):

    nuevo_stock: int = Field(gt=0)



class UsuarioCrear(BaseModel):

    usuario: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8)



class UsuarioRespuesta(BaseModel):

    model_config = ConfigDict(from_attributes=True)
    
    id: int
    usuario: str



class TokenRespuesta(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    access_token: str
    token_type: str = "bearer"



class CantidadCompra(BaseModel):

    cantidad: int = Field(gt=0)



class RespuestaCompra(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    producto_id: int
    cantidad: int
    total: Decimal
