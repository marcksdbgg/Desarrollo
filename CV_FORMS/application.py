from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cv", methods=["POST"])
def cv():
    nombres = request.form.get("nombres")
    apellidos = request.form.get("apellidos")
    direccion = request.form.get("direccion")
    correo = request.form.get("correo")
    celular = request.form.get("celular")
    presentacion = request.form.get("presentacion")
    puesto = request.form.get("puesto")
    empresa = request.form.get("empresa")
    trabajo = request.form.get("trabajo")
    univiersidad = request.form.get("universidad")
    grado_universitario = request.form.get("grado_universitario")
    titulo = request.form.get("titulo")
    h1 = request.form.get("h1")
    h2 = request.form.get("h2")
    h3 = request.form.get("h3")
    h4 = request.form.get("h4")
    metas = request.form.get("metas")

    return render_template("CV.html", nombres=nombres, apellidos=apellidos, direccion=direccion, correo=correo, celular=celular, presentacion=presentacion, puesto=puesto, empresa=empresa, trabajo=trabajo, univiersidad=univiersidad, grado_universitario=grado_universitario, titulo=titulo, h1=h1, h2=h2, h3=h3, h4=h4, metas=metas)
