from flask import Flask, request, jsonify
from db.consultas import (cabania_consultas_sql,
                          reserva_consultas_sql, imagenes_consultas)
from errors import CampoInvalido
from utils import admin

app = Flask(__name__)


@app.route("/")
def index():
    return """
        <h1>Index de API</h1>
        <p>Si necesitas un poco de ayuda, consulta la documentación</p>
    """


@app.route("/cabanias", methods=["GET"])
def cabanias():
    res = cabania_consultas_sql.obtener_cabanias()
    print("CABANIAS:", res)
    return jsonify(res), 200


@app.route("/cabanias", methods=["POST"])
@admin
def cabanias_post():
    """
    Recibe:
    {
        "secreto"
        "id"
        "nombre"
        "descripcion"
        "cap_max"
        "precio_noche"
    }
    """
    consulta = request.get_json()
    try:
        condiciones_rechazo = [
            consulta["id"] in ("", None),
            consulta["nombre"] in ("", None),
            consulta["cap_max"] < 1,
            consulta["precio_noche"] < 0
        ]
        if any(condiciones_rechazo):
            raise CampoInvalido
        exito = cabania_consultas_sql.agregar_cabania(consulta["id"],
                                                      consulta["nombre"],
                                                      consulta["descripcion"],
                                                      consulta["cap_max"],
                                                      consulta["precio_noche"])
    except KeyError:
        return jsonify({"mensaje": "No estan todos los campos"}), 400
    except CampoInvalido:
        return jsonify({"mensaje": "alguno de los campos es inválido"}), 400
    except Exception as e:
        return jsonify({"mensaje": f"FRACASO: {e}"}), 400
    if exito:
        return jsonify({"mensaje": "EXITO"}), 201
    else:
        return jsonify({"mensaje": "FRACASO"}), 400


@app.route("/cabanias/<string:id>", methods=["PATCH", "DELETE"])
@admin
def cabanias_patch_del(id):
    if request.method == "PATCH":
        """
        Recibe:
        {
            "secreto"
            "nombre"
            "descripcion"
            "cap_max"
            "precio_noche"
        }
        """
        if id is None:
            return jsonify({"mensaje": "no se pasó el id"}), 400
        try:
            consulta = request.get_json()
            condiciones_rechazo = [
                consulta["nombre"] in ("", None),
                consulta["cap_max"] < 1,
                consulta["precio_noche"] < 0
            ]

            if any(condiciones_rechazo):
                raise CampoInvalido
            exito = cabania_consultas_sql.modificar_cabania(id, consulta["nombre"],
                                                            consulta["descripcion"],
                                                            consulta["cap_max"],
                                                            consulta["precio_noche"])
        except KeyError:
            return jsonify({"mensaje": "No estan todos los campos"}), 400
        except CampoInvalido:
            return jsonify({"mensaje": "alguno de los campos es inválido"}), 400
        except Exception as e:
            return jsonify({"mensaje": f"FRACASO: {e}"}), 400

        if exito:
            return jsonify({"mensaje": "EXITO"}), 201
        else:
            return jsonify({"mensaje": "FRACASO"}), 400
    elif request.method == "DELETE":
        """
        Recibe: id (por URI)
        """
        exito = False
        try:
            if id is not None:
                exito = cabania_consultas_sql.eliminar_cabania(id)
        except Exception as e:
            return jsonify({"mensaje": f"FRACASO {e}"}), 400

        if exito:
            return jsonify({"mensaje": "EXITO"}), 201
        else:
            return jsonify({"mensaje": "FRACASO"}), 400


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
                "codigo_reserva": codigo_reserva,
                "nombre_cabania": nombre_cabania,
                "fecha_ingreso": fecha_ingreso,
                "fecha_egreso": fecha_egreso
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
            "dni": dni,
            "telefono": telefono,
            "email" : "example@example.com"
        }
    """
    res = request.get_json()
    id = res['cabania_id']
    ingreso = res['fecha_ingreso']
    egreso = res['fecha_egreso']
    dni = res['dni']
    telefono = res['telefono']
    email = res['email']
    # Falta consultar la disponibilidad antes de crear la reserva.
    codigo_reserva = consultas_sql.realizar_reserva(
        id, ingreso, egreso, dni, telefono, email)
    if codigo_reserva:
        return jsonify([{"codigo_reserva": codigo_reserva}]), 201

    return jsonify([{"mensaje": "Se a producido un error al intentar crear la reserva."}])


@app.route("/reserva/<int:id>", methods=["DELETE"])
def eliminar_reserva(id):
    """
    Recibe:
        {   
            "dni": dni,
            "telefono": telefono,
            "email" : "example@example.com"
        }
    """
    res = request.get_json()
    dni = res['dni']
    telefono = res['telefono']
    email = res['email']

    if not consultar_reserva(dni, telefono, email):
        return jsonify([{"mensaje": f"La reserva con codigo #{id} no existe."}]), 404

    if not eliminar_reserva(id, dni, email):
        return jsonify([{"mensaje": f"La reserva con codigo #{id} no corresponde con los datos proporcionados."}]), 403

    return jsonify({"mensaje": f"La reserva con codigo #{id} se a eliminado exitosamente."}), 202


if __name__ == "__main__":
    # 0.0.0.0 y debug=false para acceso publico
    app.run("127.0.0.1", port="5000", debug=True)
