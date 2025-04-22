import pandas as pd
import os

#Ruta del archivo Excel
EXCEL_PATH = os.getenv("EXCEL_PATH", "data/archivo.xlsx")

#Funcion para buscar un producto en el archivo Excel y devolver su información
def buscar_producto(nombre: str) -> str:
    try:
        df = pd.read_excel(EXCEL_PATH)
        resultado = df[df["Producto"].str.contains(nombre, case=False, na=False)]
        if resultado.empty:
            return f"No se encontró ningún producto que coincida con: {nombre}"
        else:
            return resultado.to_string(index=True)
    except Exception as e:
        return f"Error al leer Excel: {e}"
    
#Funcion para obtener todos los productos del archivo Excel y devolver su información    
def obtener_todos() -> str:
    try:
        df = pd.read_excel(EXCEL_PATH)
        return df.to_string(index=False)
    except Exception as e:
        return f"Error al leer Excel: {e}"

#Funcion para insertar un nuevo producto en el archivo Excel y devolver un mensaje de éxito o error
def insertar_producto(producto: str, precio: float, stock: int) -> str:
    try:
        df = pd.read_excel(EXCEL_PATH)
        nuevo = pd.DataFrame([{"Producto": producto, "Precio": precio, "Stock": stock}])
        df = pd.concat([df, nuevo], ignore_index=True)
        df.to_excel(EXCEL_PATH, index=False)
        return f"Producto '{producto}' insertado exitosamente."
    except Exception as e:
        return f"Error al insertar producto: {e}"
#Funcion para actualizar un producto en el archivo Excel y devolver un mensaje de éxito o error
def actualizar_producto(nombre: str, nuevo_precio: float = None, nuevo_stock: int = None) -> str:
    try:
        df = pd.read_excel(EXCEL_PATH)
        coincidencias = df["Producto"].str.contains(nombre, case=False, na=False)
        if not coincidencias.any():
            return f"No se encontró ningún producto llamado '{nombre}' para actualizar."

        if nuevo_precio is not None:
            df.loc[coincidencias, "Precio"] = nuevo_precio
        if nuevo_stock is not None:
            df.loc[coincidencias, "Stock"] = nuevo_stock

        df.to_excel(EXCEL_PATH, index=False)
        return f"Producto(s) '{nombre}' actualizado(s) correctamente."
    except Exception as e:
        return f"Error al actualizar producto: {e}"
#Funcion para eliminar un producto del archivo Excel y devolver un mensaje de éxito o error
def eliminar_producto(nombre: str) -> str:
    try:
        df = pd.read_excel(EXCEL_PATH)
        original_count = len(df)
        df = df[~df["Producto"].str.contains(nombre, case=False, na=False)]
        final_count = len(df)

        if original_count == final_count:
            return f"No se encontró ningún producto llamado '{nombre}' para eliminar."
        
        df.to_excel(EXCEL_PATH, index=False)
        return f"Producto(s) '{nombre}' eliminado(s) correctamente."
    except Exception as e:
        return f"Error al eliminar producto: {e}"
