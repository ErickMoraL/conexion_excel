from mcp.server.fastmcp import FastMCP
import excel_crud as crud

# Crea una instancia del servidor MCP con el nombre "excel-server"
mcp = FastMCP("excel-server")

# Define una herramienta MCP que busca un producto por nombre en el archivo Excel
@mcp.tool()
def buscar_producto(nombre: str) -> str:
    return crud.buscar_producto(nombre)

# Define una herramienta MCP que inserta un nuevo producto en el archivo Excel
@mcp.tool()
def insertar_producto(producto: str, precio: float, stock: int) -> str:
    return crud.insertar_producto(producto, precio, stock)

# Define una herramienta MCP que actualiza el precio y/o el stock de un producto existente
@mcp.tool()
def actualizar_producto(nombre: str, nuevo_precio: float = None, nuevo_stock: int = None) -> str:
    return crud.actualizar_producto(nombre, nuevo_precio, nuevo_stock)

# Define una herramienta MCP que elimina un producto del archivo Excel
@mcp.tool()
def eliminar_producto(nombre: str) -> str:
    return crud.eliminar_producto(nombre)

# Punto de entrada del script
# Si se ejecuta directamente, inicia el servidor MCP y espera conexiones por stdio
if __name__ == "__main__":
    print("[MCP] Servidor MCP en marcha. Esperando conexiones...")
    mcp.run(transport="stdio")
