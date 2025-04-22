from fastapi import FastAPI, Query
from pydantic import BaseModel
import excel_crud


app = FastAPI()

# Modelos para verficar la entrada de datos
class InsertarProductoRequest(BaseModel):
    producto: str
    precio: float
    stock: int
    class Config:
        extra = 'forbid' #No permite campos adicionales en la solicitud

class ActualizarProductoRequest(BaseModel):
    nombre: str
    nuevo_precio: float | None = None
    nuevo_stock: int | None = None

    class Config:
        extra = 'forbid' #No permite campos adicionales en la solicitud

# Lectura por producto
@app.get("/buscar_producto")
def buscar_producto(nombre: str = Query(..., description="Nombre del producto a buscar")):
    return {"resultado": excel_crud.buscar_producto(nombre)}

# Lectura general
@app.get("/obtener_registros")
def obtener_registros():
    return {"resultado": excel_crud.obtener_todos()}

# Inserción
@app.post("/insertar_producto")
def insertar_producto(req: InsertarProductoRequest):
    return {"resultado": excel_crud.insertar_producto(req.producto, req.precio, req.stock)}

# Actualización
@app.put("/actualizar_producto")
def actualizar_producto(req: ActualizarProductoRequest):
    return {"resultado": excel_crud.actualizar_producto(req.nombre, req.nuevo_precio, req.nuevo_stock)}

# Eliminación
@app.delete("/eliminar_producto")
def eliminar_producto(nombre: str = Query(..., description="Nombre del producto a eliminar")):
    return {"resultado": excel_crud.eliminar_producto(nombre)}
