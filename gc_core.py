import os
from permisos import esta_permitido
from autoprogramacion import guardar_funcion

def generar_respuesta(prompt, historial=[]):
    if esta_permitido("aprender"):
        os.makedirs("interacciones", exist_ok=True)
        with open("interacciones/historial_temp.txt", "a", encoding="utf-8") as f:
            f.write(f"Pregunta: {prompt}\n\n")

    respuesta = f"GC AI responde a: {prompt}"

    if "crear funcion" in prompt.lower() and esta_permitido("autoprogramacion"):
        codigo = """
def nueva_funcion(x):
    return x*2
"""
        guardar_funcion(codigo, "duplicar")
        respuesta += "\n✅ Función 'duplicar' creada y lista para usar."

    return respuesta