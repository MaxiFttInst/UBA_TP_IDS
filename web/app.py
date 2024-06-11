from flask import Flask, render_template , request
import requests
import os
app = Flask(__name__)

API_URL = os.environ.get("API_URL", "http://127.0.0.1:5000")

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
    response = requests.post('https://posadabyteados.pythonanywhere.com/crear_reserva', json=data)

    print("Respuesta de la API:", response.text)

    if response.status_code == 201:
        return 'Reserva realizada correctamente'
    else:
        return 'Error al realizar la reserva'


@app.route("/reserva")
def reserva():
    cabania_id = request.args.get('cabania_id')
    return render_template("reserva.html", cabania_id=cabania_id)





if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)