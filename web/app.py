from flask import Flask, render_template , request, redirect, url_for
import requests
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