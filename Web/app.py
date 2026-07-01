from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# --- 1. RUTAS DE NAVEGACIÓN DE LAS PANTALLAS ---

# La página principal oficial de tu sistema ahora es el Login

# --- 1. RUTAS DE NAVEGACIÓN DE LAS PANTALLAS ---

# 1. Al entrar a http://127.0.0.1:5000 se abre la bienvenida (index.html)
@app.route('/')
def bienvenida():
    return render_template('index.html')

# 2. Al darle al botón "Vamos", te lleva a la selección de perfiles (home.html)
@app.route('/home')
def seleccion_perfil():
    return render_template('home.html')

# 3. Pantalla de Inicio de Sesión / Login unificado
@app.route('/login-seleccion')
def inicio_sesion():
    return render_template('InicioSesion.html')

# 4. Formularios de registro
@app.route('/registro-veterinario')
def mostrar_registro_vet():
    return render_template('Veterinario.html')

@app.route('/registro-paciente')
def mostrar_registro_paciente():
    return render_template('Paciente.html')

# 5. Paneles de citas correspondientes
@app.route('/citas-veterinario')
def ver_citas_vet():
    return render_template('citasV.html')

@app.route('/citas-paciente')
def ver_citas_paciente():
    return render_template('CitasP.html')

# --- 2. LÓGICA DE INICIO DE SESIÓN (LOGIN) ---

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    tipo_usuario = request.form.get('tipo_usuario') # 'veterinario' o 'paciente'

    conexion = sqlite3.connect('vetconnect.db')
    cursor = conexion.cursor()

    if tipo_usuario == 'veterinario':
        # Busca en la lista de veterinarios
        cursor.execute("SELECT * FROM Veterinarios WHERE email = ? AND password = ?", (email, password))
        usuario = cursor.fetchone()
        conexion.close()
        if usuario:
            return redirect(url_for('ver_citas_vet')) # Va a citasV.html
            
    elif tipo_usuario == 'paciente':
        # Busca en la lista de pacientes
        cursor.execute("SELECT * FROM Pacientes WHERE email = ? AND password = ?", (email, password))
        usuario = cursor.fetchone()
        conexion.close()
        if usuario:
            return redirect(url_for('ver_citas_paciente')) # Va a CitasP.html

    # Si los datos están mal ingresados
    return "Correo, contraseña o tipo de usuario incorrectos. <a href='/'>Volver a intentar</a>"


# --- 3. PROCESAR Y GUARDAR REGISTRO DE VETERINARIO ---

@app.route('/guardar-veterinario', methods=['POST'])
def guardar_veterinario():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    telefono = request.form.get('telefono')
    email = request.form.get('email')
    especialidad = request.form.get('especialidad')
    rol = request.form.get('rol')
    password = request.form.get('password') # Recibe la contraseña

    try:
        conexion = sqlite3.connect('vetconnect.db')
        cursor = conexion.cursor()
        
        # Crea la tabla incluyendo la columna password
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Veterinarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                apellido TEXT,
                telefono TEXT,
                email TEXT,
                especialidad TEXT,
                rol TEXT,
                password TEXT
            )
        """)
        
        cursor.execute("""
            INSERT INTO Veterinarios (nombre, apellido, telefono, email, especialidad, rol, password)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nombre, apellido, telefono, email, especialidad, rol, password))
        
        conexion.commit()
        print("¡Veterinario registrado exitosamente!")
    except Exception as e:
        print(f"Error: {e}")
        return "Error al guardar el veterinario."
    finally:
        conexion.close()

    # Al registrarse con éxito, lo redirige al Login para que inicie sesión
    return redirect(url_for('inicio'))


# --- 4. PROCESAR Y GUARDAR REGISTRO DE PACIENTE ---

@app.route('/guardar-paciente', methods=['POST'])
def guardar_paciente():
    nombre_mascota = request.form.get('nombre_mascota') or request.form.get('nombre')
    dueno = request.form.get('dueno') or request.form.get('apellido')
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        conexion = sqlite3.connect('vetconnect.db')
        cursor = conexion.cursor()
        
        # Crea la tabla de pacientes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_mascota TEXT,
                dueno TEXT,
                email TEXT,
                password TEXT
            )
        """)
        
        cursor.execute("""
            INSERT INTO Pacientes (nombre_mascota, dueno, email, password)
            VALUES (?, ?, ?, ?)
        """, (nombre_mascota, dueno, email, password))
        
        conexion.commit()
        print("¡Paciente registrado exitosamente!")
    except Exception as e:
        print(f"Error: {e}")
        return "Error al guardar el paciente."
    finally:
        conexion.close()

    # Al registrarse con éxito, lo manda al Login también
    return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.run(debug=True)