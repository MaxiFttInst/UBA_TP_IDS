from flask import Flask, request, jsonify
from db.consultas import cabania_consultas_sql, reserva_consultas_sql, imagenes_consultas

app = Flask(__name__)

@app.route("/")
def index():
    return """
        <h1>Index de API</h1>
        <p>Si necesitas un poco de ayuda, consulta la documentación</p>
    """
#--CABANIAS--
@app.route("/cabanias", methods=["GET"])
def cabanias():
    res = cabania_consultas_sql.obtener_cabanias()
    print("CABANIAS:", res)
    return jsonify(res), 200

#--RESERVAS--
@app.route("/reserva", methods=["GET"])
def consultar_reserva():
    """
    Recibe:
        {   
            "dni": dni|pasaporte,
            "nombre_completo" : nombre_cliente
        }
    """
    consulta = request.get_json()
    dni = consulta['dni']
    nombre = consulta['nombre_completo']
    
    res = reserva_consultas_sql.consultar_reservas(dni, nombre)
    if res:
        data = []
        for codigo_reserva, nombre_cabania, fecha_ingreso, fecha_egreso in res:
            data.append({
                "codigo_reserva" : codigo_reserva,
                "nombre_cabania" : nombre_cabania,
                "fecha_ingreso": fecha_ingreso,
                "fecha_egreso" : fecha_egreso
            })
        return jsonify(data)
    
    return jsonify({"mensaje": f"No hay reservas a nombre de {nombre}."}), 404

@app.route("/crear_reserva", methods=["POST"])
def crear_reserva():
    """
    Recibe:
        {   
            "cabania_id" : id,
            "fecha_ingreso" : "aaaa-mm-dd",
            "fecha_egreso" : "aaaa-mm-dd",
            "nombre_cliente" : "nombre_cliente",
            "dni": dni,
            "telefono": telefono,
            "email" : "example@example.com"
        }
    """
    res = request.get_json()
    id = res['cabania_id']
    ingreso = res['fecha_ingreso']
    egreso = res['fecha_egreso']
    nombre = res['nombre_cliente']
    dni = res['dni']
    telefono = res['telefono']
    email = res['email']
    #revisar funcion consultar_disponibilidad()
    codigo_reserva = reserva_consultas_sql.realizar_reserva(id, ingreso, egreso, dni, nombre, telefono, email)
    print('CODIGO RESERVA:', codigo_reserva)
    if codigo_reserva:
        return jsonify({"codigo_reserva" : codigo_reserva}), 201
    
    return jsonify({"mensaje" : "Se a producido un error al intentar crear la reserva."}), 400
    
@app.route("/reserva/<int:id>", methods=["DELETE"])
def eliminar_reserva(id):
    #"""
    # Recibe:
    #     {   
    #         "dni": dni,
    #         "telefono": telefono,
    #         "email" : "example@example.com"
    #     }
    # """
    # res = request.get_json()
    # dni = res['dni']
    # telefono = res['telefono']
    # email = res['email']

    # if not consultar_reserva(dni, telefono, email):
    #     return jsonify([{"mensaje": f"La reserva con codigo #{id} no existe."}]), 404

    if reserva_consultas_sql.eliminar_reserva(id):
        return jsonify({"mensaje" : f"La reserva con codigo #{id} se a eliminado exitosamente."}), 202
    
    return jsonify({"mensaje": f"La reserva con codigo #{id} no existe."}), 404
    # if not eliminar_reserva(id):
    #     return jsonify([{"mensaje": f"La reserva con codigo #{id} no corresponde con los datos proporcionados."}]), 403

    

#--IMAGENES--

    
if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True) # 0.0.0.0 y debug=false para acceso publico
