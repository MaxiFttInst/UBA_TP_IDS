from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from db.db import obtener_reservas, obtener_habitaciones

app = Flask(__name__)

@app.route("/")
def index():
    return """
        <h1>Index de API</h1>
        <p>Si necesitas un poco de ayuda, consulta la documentación</p>
    """

@app.route("/habitaciones", methods=["GET"])
def habitaciones():
    result = obtener_habitaciones()
    data = []
    for row in result:
        entity = {}
        entity['id'] = row.habitacion_id
        entity['nombre'] = row.habitacion_nombre
        entity['descripcion'] = row.habitacion_descripcion
        entity['precio_dia'] = row.habitacion_precio_dia
        data.append(entity)

    return jsonify(data), 200

@app.route("/reservas", methods=["GET"])
def reservas():
    result = obtener_reservas()
    pass

@app.route("/crear_reserva/<int:id>", methods=["POST"])
def crear_reserva(id):
    pass

@app.route("/reservas/<int:id>", methods=["DELETE"])
def eliminar_reserva(id):
    #eliminar_r(id)
    pass

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True) # 0.0.0.0 y debug=false para acceso publico
