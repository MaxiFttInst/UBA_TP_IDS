from settings import API_URL
from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import datetime
import os
import utils
import datetime
app = Flask(__name__)
app.secret_key = b'clave_secreta_byteados'  # necesaria para usar flash


UBICACION = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3424.447722353874!2d-64.52246542441412!3d-30.87413387451641!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9432a3be8784d545%3A0x3117451a980afefd!2sCaba%C3%B1as%20La%20Morada%20De%20La%20Luna!5e0!3m2!1ses!2sar!4v1717986682657!5m2!1ses!2sar"


@app.route("/")
def index():
    res = requests.get(API_URL + "/cabanias")
    cabanias = {}
    imagenes = []
    instalacionesComunes = {"Pileta común": ["Para dias calurosos podras disfrutar de nuestra piscina!!", 'Imagenes/pileta.jpg'], "Sala de SPA": ["Una increible sala de spa para que puedas relajarte despues de un dia muy largo de haber conocido la zona!!", 'Imagenes/spa.jpg'],
                            "Arcade con cocina": ["Podras disfrutar de todos los juegos que tenemos para ti! pool, videojuegos, television, metegol y muchos juegos de mesa!!", 'Imagenes/juegos.jpg']}

    if res.status_code == 200:
        cabanias = res.json()

    for cabania in cabanias:
        if "portada" in cabanias[cabania]["imagenes"]:
            imagenes.append(cabanias[cabania]["imagenes"]["portada"])

    return render_template("index.html", cabanias=cabanias, lista_carrucel=imagenes, ubicacion=UBICACION, dic_espacios=instalacionesComunes)


# Ruta para manejar la solicitud de reserva
@app.route('/reservar', methods=['POST'])
def forms_reserva():
    # Obtener los datos del formulario
    data = {
        'cabania_id': request.form['cabania_id'],
        'fecha_ingreso': request.form['fcheckin'],
        'fecha_egreso': request.form['fcheckout'],
        'nombre_cliente': request.form['fname'],
        'cliente_id': request.form['fdni'],
        'telefono': request.form['fnumber'],
        'email': request.form['femail'],

    }
    print(data)

    # Realizar la solicitud POST a la API del backend
    response = requests.post(
        f'{API_URL}/crear_reserva', json=data)

    if response.status_code == 201:
        codigo_reserva = response.json().get('codigo_reserva')
        flash('EXITO')  # Configurar el mensaje flash
        return render_template("reserva_exitosa.html", codigo_reserva=codigo_reserva)
    else:
        flash('ERROR')
        return render_template("reserva_fallida.html")


@app.route('/cancelar', methods=['POST'])
def forms_cancelacion():
    reserva_id = request.form['reserva_id']
    mail_cancelacion = request.form['mail_cancelacion']
    # Obtener los datos del formulario

    data = {
        'reserva_id': reserva_id,
        'email': mail_cancelacion
    }
    print(data)
    # Realizar la solicitud POST a la API del backend
    response = requests.delete(
        f'{API_URL}/reserva/{reserva_id}', json=data)

    print("Respuesta de la API:", response.text)

    if response.status_code == 202:
        flash('EXITO')
        return render_template("cancelacion_exitosa.html")
    else:
        flash('ERROR')
        return render_template("cancelacion_fallida.html")


@app.route('/consultar-reserva', methods=['POST'])
def form_consultar_reservas():
    nombre_cliente = request.form['fname']
    id_cliente = request.form['fdni']

    # Obtener los datos del formulario
    data = {
        "cliente_id": id_cliente,
        "nombre_cliente": nombre_cliente
    }

    # Realizar la solicitud POST a la API del backend
    response = requests.get(API_URL + "/reserva", json=data)
    response = response.json()
    print("Respuesta de la API:", response)
    if "msj" in response:
        return render_template("cancelacion.html", ubicacion=UBICACION, reservas=response, len=-1)
    else:
        return render_template("cancelacion.html", ubicacion=UBICACION, reservas=response, len=len(response))


@app.route("/reserva")
def reserva():
    nombres_meses = ["", "enero", "febrero", "marzo", "abril",
                     "mayo", "junio", "julio", "agosto",
                     "septiembre", "ocbutbre", "noviembre", "diciembre"]
    cabania_id = request.args.get('cabania_id')
    mes = request.args.get('mes')
    año = request.args.get('año')
    mes_anterior: int = None
    mes_siguiente: int = None
    if mes is not None:
        mes = int(mes)
    if año is not None:
        año = int(año)

    mes, año, calendario_data = utils.obtener_calendario(cabania_id, mes, año)
    print(mes)
    mes_anterior = mes - 1
    mes_siguiente = mes + 1
    return render_template("reserva.html",
                           cabania_id=cabania_id,
                           mes_anterior=mes_anterior,
                           mes_siguiente=mes_siguiente,
                           mes=mes,
                           nombres_meses=nombres_meses,
                           año=año,
                           ubicacion=UBICACION,
                           calendario_data=calendario_data)


@app.route("/cancelar")
def cancelar():
    return render_template("cancelacion.html", ubicacion=UBICACION, reservas=[], len=0)


@app.route("/reserva_exitosa")
def reserva_exitosa():
    return render_template("reserva_exitosa.html")


if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)
