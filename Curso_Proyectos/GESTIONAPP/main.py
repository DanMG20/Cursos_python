from flask import Flask , render_template , redirect, session, request
import datos
import psycopg2
import os
from datetime import datetime
#Instancia de Flask
app = Flask(__name__)
app.secret_key = os.urandom(24)
conexion = psycopg2.connect(host=datos.HOST,
                                   user=datos.USER,
                                   password=datos.PASSWORD,
                                   database=datos.DATABASE)
#intermediario que permite hacer consultas en la db
cursor = conexion.cursor()


@app.route("/")

def login():
    return render_template("login.html")

@app.route("/cerrar_sesion")

def cerrar_sesion():
    session.pop("id")
    return redirect("/")


@app.route("/agregar_movimiento" ,methods =["POST"])
def agregar_movimiento():
    descripcion = request.form.get("descripcion")
    monto = request.form.get("monto")
    tipo = request.form.get("tipo")
    fecha = datetime.now().strftime("%Y-%M,%D")
    if "id" in session:
        id_usuario = session["id"]
        cursor.execute("INSERT INTO movimientos (id_usuario, descripcion, monto, tipo , fecha) VALUES (%s,%s,%s,%s,%s)", (id_usuario,descripcion,monto,tipo,fecha))
        conexion.commit()
    return redirect("/home")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/agregar_usuario", methods=["POST"])

def agregar_usuario():
    nombre =request.form.get("unombre")
    email= request.form.get("uemail")
    password =request.form.get("upassword")

    cursor.execute(
        'INSERT INTO usuarios_gestionapp ("Nombre", "email", "password") VALUES (%s, %s, %s)',
        (nombre, email, password)
    )
    conexion.commit()
    return "Usuario registrado exitosamente"








@app.route("/home")

def home():
    if "id" in session:
        id_usuario = session["id"]

        cursor.execute("SELECT SUM(monto) FROM movimientos WHERE id_usuario = %s AND tipo = \'ingreso' ", (id_usuario,))
        total_ingresos= cursor.fetchone()[0] or 0


        cursor.execute("SELECT SUM(monto) FROM movimientos WHERE id_usuario = %s AND tipo = \'Egreso' ", (id_usuario,))
        total_egresos= cursor.fetchone()[0] or 0

        saldo_total = total_ingresos - total_egresos

        cursor.execute("SELECT descripcion, monto, tipo, fecha FROM movimientos WHERE id_usuario = %s", (id_usuario,))
        movimientos = cursor.fetchall()
        return render_template("home.html",
                               total_ingresos =total_ingresos,
                               total_egresos= total_egresos,
                               saldo_total = saldo_total,
                               movimientos = movimientos)
    else:
        return redirect("/")



@app.route("/validacion_login", methods=["POST"])

def validacion_login():
    email = request.form.get("email")
    password = request.form.get("password")

    cursor.execute("SELECT * FROM usuarios_gestionapp WHERE email = %s AND password = %s", (email,password))
    usuarios = cursor.fetchall()

    if len(usuarios) >0:
        session["id"] =usuarios[0][0]
        return redirect("/home")
    else:
        return redirect("/")
    return usuarios


@app.route("/perfil")

def perfil():
    if "id" in session:
        id_usuario = session["id"]
        cursor.execute('SELECT "Nombre", email FROM usuarios_gestionapp WHERE id_usuario = %s', (id_usuario,))
        usuario = cursor.fetchone()
        return render_template("/perfil.html",
                               usuario = usuario,
                               )
    else:
        return redirect("/")


@app.route("/analisis")

def analisis():
    if "id" in session:
        id_usuario = session["id"]

        cursor.execute("SELECT descripcion, monto, tipo, fecha FROM movimientos WHERE id_usuario = %s", (id_usuario,))
        movimientos = cursor.fetchall()
        return render_template("/analisis.html",
                               movimientos = movimientos)
    else:
        return redirect("/")



# se asegura que solo se ejecute si se corre directamente
if __name__ == "__main__":
    app.run(debug=True)