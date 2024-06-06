from flask import Flask, render_template , request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    imagenes=["Imagenes/habitacion1.jpg","Imagenes/habitacion2.jpg","Imagenes/habitacion3.jpg"]
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


        print(ingreso)
        print(salida)
        print(nombre)
        print(mail)
        print(dni)
        print(numero_telefonico)
        return render_template("habitacion2.html")


@app.route("/reserva")
def habitacion_1():
    return render_template("reserva.html")


@app.route("/habitacion2")
def habitacion_2():
    return render_template("habitacion2.html")


@app.route("/habitacion3")
def habitacion_3():
    return render_template("habitacion3.html")


if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)