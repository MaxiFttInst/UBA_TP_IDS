from flask import Flask, render_template , request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    imagenes=["Imagenes/presencialunarportada.jpg","Imagenes/vicariaameliaportada.jpg","Imagenes/bestiaclerigoportada.jpg","Imagenes/emisariocelestialportada.jpg","Imagenes/adelaportada.jpg","Imagenes/almendraportada.jpg"]
    return render_template("base.html",lista=imagenes)


@app.route("/..", methods=["GET", "POST"])
def algo():
    if request.method == "POST":
        nombre = request.form.get("fname")
        email = request.form.get("email")
        mensaje = request.form.get("msj")
        return render_template("succesful_form.html", name=nombre, email=email,msg=mensaje)
    return render_template("base.html")

@app.route("/formulario_reserva",methods=["POST"])
def reserva():
    if request.method == "POST":   
        ingreso = request.form.get("fcheckin")
        salida = request.form.get("fcheckout")
        nombre = request.form.get("fname")
        mail = request.form.get("femail")
        dni = request.form.get("fdni")
        numero_telefonico = request.form.get("fnumber")


@app.route("/habitacion1")
def habitacion_1():
    return render_template("habitacion1.html")

if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)