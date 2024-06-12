from flask import Flask, render_template , request
import requests
import os
import utils

app = Flask(__name__)

API_URL = os.environ.get("API_URL", "https://posadabyteados.pythonanywhere.com")

@app.route("/")
def index():
    res = requests.get(API_URL + "/cabanias")
    cabanias = {}

    if res.status_code == 200:
        cabanias = res.json()

    return render_template("base.html", cabanias=cabanias)


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
    response = requests.post(f"{API_URL}/crear_reserva", json=data)

    if response.status_code == 201:
        codigo_reserva = response.json().get('codigo_reserva')
        print(codigo_reserva)
        return 'Reserva realizada correctamente'
    else:
        return render_template("form_fallido.html")


@app.route('/cancelar', methods=['POST'])
def forms_cancelacion():
    reserva_id =  request.form['reserva_id']
    mail_cancelacion =  request.form['mail_cancelacion']
    # Obtener los datos del formulario
    
    data = {
        'email': mail_cancelacion
    }
    print(data)
    # Realizar la solicitud POST a la API del backend
    response = requests.delete(f'https://posadabyteados.pythonanywhere.com/reserva/{reserva_id}', json=data)

    print("Respuesta de la API:", response.text)

    if response.status_code == 202:
        return 'Cancelacion realizada correctamente'
    else:
        return 'Error al cancelar la reserva'

@app.route("/reserva")
def reserva():
    cabania_id = request.args.get('cabania_id')
    calendario_data = utils.obtener_calendario(cabania_id)
    return render_template("reserva.html", cabania_id=cabania_id, calendario_data=calendario_data)


@app.route("/cancelar")
def cancelar():
    return render_template("cancelacion.html")


@app.route("/exito")
def exito():
    return render_template("form_exitoso.html")


@app.route("/cancelacion_fallida")
def cancelacion_fallida():
    return render_template("form_fallido.html")

    return render_template("reserva.html", cabania_id=cabania_id, calendario_data=calendario_data)

if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)
