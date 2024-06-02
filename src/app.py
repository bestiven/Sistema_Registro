from flask import Flask, flash, render_template, request, redirect, url_for
from config import *
from bd import *

## Crear instancia de conexión a la base de datos y debe ir antes de crear la instancia de la aplicación
con_bd = Conexion()

app = Flask(__name__)
app.secret_key = 'dhshfdedgfbilewgefilh'

@app.route('/')
def home():
    return render_template("registro.html")

@app.route('/administrar')
def index():
    colection_aspirantes = con_bd['aspirantes']
    aspirantesRegistrados = colection_aspirantes.find()
    return render_template("administrar_aspirantes.html", aspirantes=aspirantesRegistrados)

@app.route('/registrar')
def registrar():
    return render_template("registrar_aspirante.html")

@app.route('/guardar_aspirantes', methods=['POST'])
def agregaraspirantes():
    colection_aspirantes = con_bd['aspirantes']
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    tipo_doc = request.form['tipo_doc']
    documento = request.form['documento']
    telefono = request.form['telefono']
    correo = request.form['correo']
    genero = request.form['genero']
    carrera = request.form['carrera']
    if nombres and apellidos and tipo_doc and documento and telefono and correo and genero and carrera:
        object_aspirantes = {
            'nombres': nombres,
            'apellidos': apellidos,
            'tipo_doc': tipo_doc,
            'documento': documento,
            'telefono': telefono,
            'correo': correo,
            'genero': genero,
            'carrera': carrera
        }
        colection_aspirantes.insert_one(object_aspirantes)
        flash("Registro Guardado Correctamente", "info")
        return redirect(url_for('index'))
    else:
        return "Error"

## Ruta para eliminar un dato
@app.route('/eliminar_aspirantes/<string:documento>')
def eliminar(documento):
    colection_aspirantes = con_bd['aspirantes']
    colection_aspirantes.delete_one({'documento': documento})
    flash("Registro Eliminado Correctamente", "info")
    return redirect(url_for('index'))

@app.route("/editar_aspirantes/<string:documento>", methods=['GET', 'POST'])
def editar(documento):
    colection_aspirantes = con_bd['aspirantes']
    aspirante = colection_aspirantes.find_one({'documento': documento})
    
    if request.method == 'POST':
        nombres = request.form.get('nombres')
        apellidos = request.form.get('apellidos')
        tipo_doc = request.form.get('tipo_doc')
        nuevo_documento = request.form.get('documento')
        telefono = request.form.get('telefono')
        correo = request.form.get('correo')
        genero = request.form.get('genero')
        carrera = request.form.get('carrera')
        if nombres and apellidos and tipo_doc and nuevo_documento and telefono and correo and genero and carrera:
            colection_aspirantes.update_one(
                {'documento': documento},
                {'$set': {
                    'nombres': nombres,
                    'apellidos': apellidos,
                    'tipo_doc': tipo_doc,
                    'documento': nuevo_documento,
                    'telefono': telefono,
                    'correo': correo,
                    'genero': genero,
                    'carrera': carrera
                }}
            )
            flash("Registro Actualizado Correctamente", "info")
            return redirect(url_for('index'))
        else:
            return "Error: Todos los campos son obligatorios"
    else:
        return render_template('administrar_aspirantes.html', aspirante=aspirante)

if __name__== '__main__':
    app.run(debug=True, port=7777)

