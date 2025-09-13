permisos_ia = {
    "autoprogramacion": True,
    "aprender": True,
    "ejecutar_codigo": True,
    "graficos": True,
    "resumen_explicacion": True
}

def set_permiso(nombre, valor):
    if nombre in permisos_ia:
        permisos_ia[nombre] = valor
        return f"✅ Permiso '{nombre}' actualizado a {valor}"
    return f"⚠️ Permiso '{nombre}' no existe"

def esta_permitido(nombre):
    return permisos_ia.get(nombre, False)