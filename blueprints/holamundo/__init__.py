from flask import Blueprint, redirect,render_template

#inicializar un blueprint

holamundo_bp=Blueprint("holamundo",__name__,template_folder="templates")

@holamundo_bp.route("/")
def index():
    return "Hola mundo desde Blueprint"

@holamundo_bp.route("/hola/<nombre>")
def hola_nombre(nombre):
    return "Hola "+nombre+" Bienvenido"

@holamundo_bp.route("/Holahtml")
def hola_html():
    return render_template("hola.html")

