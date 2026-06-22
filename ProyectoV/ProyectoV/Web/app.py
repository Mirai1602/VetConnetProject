from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


# --- 1. CONFIGURACIÓN E INICIALIZACIÓN DE LA BASE DE DATOS ---

def inicializar_base_de_datos():
    conexion = sqlite3.connect('vetconnect.db')
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Veterinarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT, apellido TEXT, telefono TEXT, email TEXT, especialidad TEXT, rol TEXT, password TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_mascota TEXT, dueno TEXT, email TEXT, password TEXT
        )
    """)
    conexion.commit()
    conexion.close()

# Se ejecuta automáticamente al arrancar la aplicación
inicializar_base_de_datos()


# --- 2. RUTAS DE NAVEGACIÓN DE LAS PANTALLAS ---

@app.route('/')
def bienvenida():
    return render_template('index.html')

@app.route('/home')
def seleccion_perfil():
    return render_template('home.html')

@app.route('/login-seleccion')
def inicio_sesion():
    return render_template('InicioSesion.html')

@app.route('/registro-veterinario')
def mostrar_registro_vet():
    return render_template('Veterinario.html')

@app.route('/registro-paciente')
def mostrar_registro_paciente():
    return render_template('Paciente.html')

@app.route('/citas-paciente')
def citas_paciente():
    return render_template('CitasP.html')

@app.route('/citas-veterinario')
def citas_veterinario():
    return render_template('citasV.html')


# --- 3. LÓGICA DE INICIO DE SESIÓN (LOGIN) ---

@app.route('/login', methods=['POST'])
def login():
    # 1. Primero capturamos los datos del formulario
    email = request.form.get('email')
    password = request.form.get('password')
    tipo_usuario = request.form.get('tipo_usuario') 

    conexion = sqlite3.connect('vetconnect.db')
    cursor = conexion.cursor()

    # 2. Si es Veterinario, validamos y redirigimos a su FUNCIÓN correspondiente
    if tipo_usuario == 'veterinario':
        cursor.execute("SELECT * FROM Veterinarios WHERE email = ? AND password = ?", (email, password))
        usuario = cursor.fetchone()
        conexion.close()
        if usuario:
            # Redirige a def citas_veterinario()
            return redirect(url_for('citas_veterinario'))
            
    # 3. Si es Paciente, validamos y redirigimos a su FUNCIÓN correspondiente
    elif tipo_usuario == 'paciente':
        cursor.execute("SELECT * FROM Pacientes WHERE email = ? AND password = ?", (email, password))
        usuario = cursor.fetchone()
        conexion.close()
        if usuario:
            # Redirige a def citas_paciente()
            return redirect(url_for('citas_paciente'))

    # 4. Si los datos no coinciden o la base de datos se cerró sin entrar a los "if"
    return "Correo, contraseña o tipo de usuario incorrectos. <a href='/login-seleccion'>Volver a intentar</a>"