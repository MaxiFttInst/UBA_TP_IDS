from flask import Flask, render_template , request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    imagenes=["Imagenes/presencialunarportada.jpg","Imagenes/vicariaameliaportada.jpg","Imagenes/bestiaclerigoportada.jpg","Imagenes/emisariocelestialportada.jpg","Imagenes/adelaportada.jpg","Imagenes/almendraportada.jpg"]
    return render_template("base.html",lista=imagenes)

@app.route("/formulario_reserva",methods=["POST"])
def reserva():
    if request.method == "POST":   
        ingreso = request.form.get("fcheckin")
        salida = request.form.get("fcheckout")
        nombre = request.form.get("fname")
        mail = request.form.get("femail")
        dni = request.form.get("fdni")
        numero_telefonico = request.form.get("fnumber")
        return render_template("habitacion2.html")


@app.route("/reserva")
def habitacion_1():
    return render_template("reserva.html")

if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)