from flask import Flask, render_template , request, redirect, url_for
import requests
app = Flask(__name__)


@app.route("/")
def index():
    imagenes=["Imagenes/presencialunarportada.jpg","Imagenes/vicariaameliaportada.jpg","Imagenes/bestiaclerigoportada.jpg",
              "Imagenes/emisariocelestialportada.jpg","Imagenes/adelaportada.jpg","Imagenes/almendraportada.jpg"]
    espacios={"Pileta común":["Para dias calurosos podras disfrutar de nuestra piscina!!",'Imagenes/pileta.jpg']
              ,"Sala de SPA":["Una increible sala de spa para que puedas relajarte despues de un dia muy largo de haber conocido la zona!!",'Imagenes/spa.jpg'],
              "Arcade con cocina":["Podras disfrutar de todos los juegos que tenemos para ti! pool, videojuegos, television, metegol y muchos juegos de mesa!!",'Imagenes/juegos.jpg']}
    ubicacion="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3424.447722353874!2d-64.52246542441412!3d-30.87413387451641!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9432a3be8784d545%3A0x3117451a980afefd!2sCaba%C3%B1as%20La%20Morada%20De%20La%20Luna!5e0!3m2!1ses!2sar!4v1717986682657!5m2!1ses!2sar"
    return render_template("base.html",lista_carrucel=imagenes,dic_espacios=espacios,ubicacion=ubicacion)


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

@app.route("/admin")
def admin():
    return render_template("admin.html")















if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)