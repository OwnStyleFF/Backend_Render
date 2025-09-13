import os

FUNCIONES_DIR = "funciones_ia"
os.makedirs(FUNCIONES_DIR, exist_ok=True)

def guardar_funcion(codigo, nombre):
    archivo = os.path.join(FUNCIONES_DIR, f"{nombre}.py")
    with open(archivo, "w", encoding="utf-8") as f:
        f.write(codigo)
    return f"✅ Función '{nombre}' guardada y lista."

def listar_funciones():
    return [f[:-3] for f in os.listdir(FUNCIONES_DIR) if f.endswith(".py")]

def cargar_funcion(nombre):
    archivo = os.path.join(FUNCIONES_DIR, f"{nombre}.py")
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return f.read()
    return None