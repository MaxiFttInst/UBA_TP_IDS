from flask import Flask, request, jsonify
import db.consultas.cabania_consultas_sql as cabania
import db.consultas.imagenes_consultas as imagen
import db.consultas.reserva_consultas_sql as reserva

from errors import CampoInvalido
from utils import admin

app = Flask(__name__)


@app.route("/")
def index():
    return """
        <h1>Index de API</h1>
        <p>Si necesitas un poco de ayuda, consulta la documentación</p>
    """
# --CABANIAS--


@app.route("/cabanias", methods=["GET"])
def cabanias():
    res = cabania.obtener_cabanias()
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
        exito = cabania.agregar_cabania(consulta["id"],
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
            exito = cabania.modificar_cabania(id,
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
    elif request.method == "DELETE":
        """
        Recibe: id (por URI)
        """
        exito = False
        try:
            if id is not None:
                exito = cabania.eliminar_cabania(id)
        except Exception as e:
            return jsonify({"mensaje": f"FRACASO {e}"}), 400

        if exito:
            return jsonify({"mensaje": "EXITO"}), 201
        else:
            return jsonify({"mensaje": "FRACASO"}), 400

# --RESERVAS--


@app.route("/reserva", methods=["GET"])
def consultar_reserva():
    """
    Recibe:
        {   
            "cliente_id": cliente_id|pasaporte,
            "nombre_cliente" : nombre_cliente
        }
    """
    try:
        consulta = request.get_json()
        cliente_id = consulta['cliente_id']
        nombre = consulta['nombre_cliente']

        res = reserva.consultar_reservas(cliente_id, nombre)
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

        return jsonify({"msj": f"No hay reservas a nombre de {nombre}."}), 404
    except KeyError:
        return jsonify({"msj": "Los campos ingresados son incorrectos."}), 400

@app.route("/crear_reserva", methods=["POST"])
def crear_reserva():
    """
    Recibe:
        {   
            "cabania_id" : id,
            "fecha_ingreso" : "aaaa-mm-dd",
            "fecha_egreso" : "aaaa-mm-dd",
            "nombre_cliente" : "nombre_cliente",
            "cliente_id": cliente_id,
            "telefono": telefono,
            "email" : "example@example.com"
        }
    """
    try:
        res = request.get_json()
        id = res['cabania_id']
        ingreso = res['fecha_ingreso']
        egreso = res['fecha_egreso']
        nombre = res['nombre_cliente']
        cliente_id = res['cliente_id']
        telefono = res['telefono']
        email = res['email']
        # revisar funcion consultar_disponibilidad()
        codigo_reserva = reserva.realizar_reserva(
            id, ingreso, egreso, cliente_id, nombre, telefono, email)
        print('CODIGO RESERVA:', codigo_reserva)
        if codigo_reserva:
            return jsonify({"codigo_reserva": codigo_reserva}), 201

        return jsonify({"mensaje": "Se a producido un error al intentar crear la reserva."}), 400
    except KeyError:
        return jsonify({"msj": "Los campos ingresados son incorrectos."}), 400

@app.route("/reserva/<int:id>", methods=["DELETE"])
@admin
def eliminar_reserva(id):
    """
    Recibe:
        {
            "secreto" : passw
        }
    """

    if reserva.eliminar_reserva(id):
        return jsonify({"mensaje": f"La reserva con codigo #{id} se a eliminado exitosamente."}), 202

    return jsonify({"mensaje": f"La reserva con codigo #{id} no existe."}), 404
   
@app.route("/reserva/<int:id>", methods=["PATCH"])
@admin
def actualizar_reserva(id):
    """
    Recibe:
    {
        "secreto" : passw
    }
    y al menos uno de los siguientes: 
    -"cabania_id" : id
    -"fecha_ingreso" : "aaaa-mm-dd"
    -"fecha_egreso" : "aaaa-mm-dd"
    -"nombre_cliente" : "nombre_cliente"
    -"cliente_id": cliente_id
    -"telefono": telefono
    -"email" : "example@example.com"

    ej:
    {
        "cliente_id" : cliente_id-modificado,
        "telefono" : telefono-actualizado
    }
    """
    res = request.get_json(silent=True)
    cabania_id = res.get("cabania_id", None)
    fecha_ingreso = res.get("fecha_ingreso", None)
    fecha_egreso = res.get("fecha_egreso", None)
    nombre_cliente = res.get("nombre_cliente", None)
    cliente_id = res.get("cliente_id", None)
    telefono = res.get("telefono", None)
    email = res.get("email", None)

    if reserva.actualizar_reserva(id, cabania_id, fecha_ingreso, fecha_egreso, nombre_cliente, cliente_id, telefono, email):
        return jsonify({"msj": "Su reserva se modifico exitosamente."}), 200

    return jsonify({"Hubo un problema al intentar modificar la reserva", 400})

# --IMAGENES--


@app.route("/imagenes", methods=["GET"])
def obtener_imagenes():
    """
    Recibe:
    {   
        "cabania_id" : id *opcional*
    }
    """
    try:
        res = request.get_json()
        id = res["cabania_id"]
        imagenes = imagen.obtener_imagenes(id)
        print("IMAGENES:", imagenes)
        return jsonify(imagenes), 200
    except:
        imagenes = imagen.obtener_imagenes()
        print("IMAGENES:", imagenes)
        return jsonify(imagenes), 200


@app.route("/crear_imagen", methods=["POST"])
@admin
def crear_imagen():
    """
    Recibe:
    {
        "secreto" : passw,
        "cabania_id" : id, *opcional*
        "link" : url_img,
        "descripcion" : portada
    }
    """
    res = request.get_json()
    cabania_id = res.get("cabania_id", None)
    link = res["link"]
    descripcion = res["descripcion"]

    fue_creada = False
    if cabania_id == None:
        fue_creada = imagen.agregar_imagen(link, descripcion)
    else:
        fue_creada = imagen.agregar_imagen(
            link, descripcion, cabania_id)

    if fue_creada:
        return jsonify({"msj": "La imagen fue agregada con exito."}), 201
    return jsonify({"msj": "Ocurrio un error al intentar crear la imagen."}), 400


@app.route("/imagen", methods=["DELETE"])
@admin
def eliminar_imagen():
    """
    Recibe:
    {   
        "secreto" : passw,
        "link" : url
    }
    """
    res = request.get_json()
    link = res['link']
    fue_eliminada = imagen.eliminar_imagen(link)

    if fue_eliminada:
        return jsonify({"msj": "La imagen se elimino exitosamente."}), 202

    return jsonify({"No se a podido eliminar la imagen."}), 400


if __name__ == "__main__":
    # 0.0.0.0 y debug=false para acceso publico
    app.run("127.0.0.1", port="5000", debug=True)
