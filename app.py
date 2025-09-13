from flask import Flask, request, jsonify
from flask_cors import CORS
from gc_core import generar_respuesta
import os

app = Flask(__name__)
CORS(app)  # Permite peticiones desde cualquier dominio
app.secret_key = os.urandom(16)
os.makedirs("sesiones", exist_ok=True)

@app.route("/api/chat", methods=["POST"])
def chat_api():
    data = request.get_json()
    pregunta = data.get("pregunta", "")
    respuesta = generar_respuesta(pregunta)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
