from fastapi import FastAPI
from rutas.productos import router as productos_router
from rutas.usuarios import router as usuarios_router
from rutas.compras import router as compras_router


app = FastAPI()

app.include_router(productos_router)
app.include_router(usuarios_router)
app.include_router(compras_router)