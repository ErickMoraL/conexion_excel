# Proyecto Piloto: MCP + Claude Desktop + N8N + Excel

## Descripción
Este proyecto es una prueba piloto que permite la edición remota de un archivo Excel local mediante operaciones CRUD, utilizando:
- Una **API REST** local (FastAPI) que expone endpoints para operar sobre un Excel.
- **Claude Desktop** como interfaz de IA conectada a un MCP (Model Context Protocol).
- Un flujo en **N8N** que conecta con **Telegram** y utiliza un agente de IA para interpretar comandos y modificarlos en Excel.

## Tecnologías utilizadas

- Python + FastAPI + pandas
- Claude Desktop + SDK MCP
- N8N (versión web)
- Telegram Bot API
- Excel local (.xlsx)

## Instalación
### 1. Clona este repositorio
```bash
git clone https://github.com/ErickMoraL/conexion_excel
cd proyecto-mcp
```
###2. Crea un entorno virtual y activa
```bash
uv venv
source .venv/bin/activate  #Linux
.venv\Scripts\activate #Windows
```
### 3. Instala dependencias
```bash
uv pip install -r pyproject.toml
```
## Arranque del servidor de la API

con tu entorno virtual activado ejecuta el siguiente comando
```bash
uvicorn api_excel:app --reload
```
para desactivar el servidor solo presiona ctrl + c

### Documentacion de la API  disponible en http://127.0.0.1:8000/docs

### Exponer el servidor mediante un tunel de cloudeflare
En Windows:

- Ir a https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/
- Descargar el instalador .exe
- Ejecutarlo. Verificá que esté funcionando con:
```bash
cloudflared --version
```
- Generacion del tunel con:
```bash
cloudflared tunnel --url http://localhost:8000
```
- Esto mostrará algo como:
```bash
Your quick Tunnel has been created! Visit it at:
https://mi-tunel-random.trycloudflare.com
```
### Usar la URL pública para consumir tu API
Ejemplo: 
```
GET https://mi-tunel-random.trycloudflare.com/obtener_registros
```


## Configurar el MCP en Claude Desktop
- Abre Claude  y presiona Ctrl + coma (,)
- Selecciona la opcion de desarrollador y editar configuracion
- Abre el archivo **claude_desktop_config.json**
- Coloca lo siguiente:

```json
{
  "mcpServers": {
    "excel-crud": {
      "command": ".../uv.exe", 
      "args": [
        "--directory",
        "C:/Users/carro/Desktop/conexion_excel",
        "run",
        "mcp_claude.py"
      ]
    }
  }
}
```

- En el elemento "command" va la ruda del archivo uv.exe, en caso de no saber su ubicacion ejecuta:

```bash
get-Command uv.exe #windows
where uv.exe #linux
```

- Reinicia Claude

## Flujo de trabajo
- El agente IA en N8N interpreta el mensaje desde Telegram.
- Genera una petición HTTP con los datos necesarios.
- La API local recibe y modifica el Excel.
- Claude Desktop también puede acceder al archivo usando el MCP y describir/modificar el contenido.




