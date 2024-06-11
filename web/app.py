from flask import Flask, render_template , request, redirect, url_for
import requests
import json
app = Flask(__name__)


@app.route("/")
def index():
    imagenes=["Imagenes/presencialunarportada.jpg","Imagenes/vicariaameliaportada.jpg","Imagenes/bestiaclerigoportada.jpg","Imagenes/emisariocelestialportada.jpg","Imagenes/adelaportada.jpg","Imagenes/almendraportada.jpg"]
    return render_template("base.html",lista=imagenes)


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