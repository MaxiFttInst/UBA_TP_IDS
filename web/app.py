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
        'habitacion_id': request.form['habitacion_id'],
        'fecha_ingreso': request.form['fcheckin'],
        'fecha_egreso': request.form['fcheckout'],
        'dni_cliente': request.form['fdni'],
        'telefono_cliente': request.form['fnumber'],
        'mail_cliente': request.form['femail'],
        'nombre_completo_cliente': request.form['fname'],
    }
    
    # Realizar la solicitud POST a la API del backend
    response = requests.post('http://localhost:5000/api/reservas', json=data)
 
    if response.status_code == 201:
        return 'Reserva realizada correctamente'
    else:
        return 'Error al realizar la reserva'


@app.route("/reserva")
def reserva():
    return render_template("reserva.html")
















if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)

    return render_template("reserva.html", cabania_id=cabania_id, calendario_data=calendario_data)

if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)
