from flask import Flask, render_template, request, redirect, url_for
import pyodbc 

app = Flask(__name__)

# --- 1. CONFIGURACIÓN DE CONEXIÓN A SQL SERVER ---
SERVIDOR = '(localdb)\\MSSQLLocalDB'  
BASE_DATOS = 'PetConnect'  # Corregido al nombre oficial de tu base de datos

def obtener_conexion():
    return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\\MSSQLLocalDB;DATABASE=VetConnet;Trusted_Connection=yes;')


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
# ❌ Así lo debes tener actualmente (con el nombre incorrecto):
conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\\MSSQLLocalDB;DATABASE=VetConnet;Trusted_Connection=yes;')
@app.route('/registro-veterinario')
def mostrar_registro_vet():
    return render_template('Veterinario.html')

conexion = obtener_conexion()
# --- 3. VISTA DE PACIENTES / TABLA CLÍNICA ---

@app.route('/citas-paciente')
def citas_paciente():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        
        # 1. Trae todos los pacientes para la tabla principal
        cursor.execute("""
            SELECT 
                p.IdMacota AS Codigo,
                p.NombreMacota AS Mascota,
                'Sin Dueño Asignado' AS Dueño, 
                r.NombreRaza AS Raza,
                p.FechaNacimiento AS [F. Nacimiento],
                p.Genero AS Género,
                p.Peso AS Peso,
                e.NombreEspecie AS Especie
            FROM Paciente p
            INNER JOIN Raza r ON p.CodigoRaza = r.CodigoRaza
            INNER JOIN Especie e ON r.CodigoEspecie = e.CodigoEspecie
        """)
        todas_las_mascotas = cursor.fetchall()
        
        # 2. CONTADOR DE PERROS (Caninos)
        cursor.execute("""
            SELECT COUNT(*) FROM Paciente p
            INNER JOIN Raza r ON p.CodigoRaza = r.CodigoRaza
            WHERE r.CodigoEspecie = 'CAN'
        """)
        total_perros = cursor.fetchone()[0]
        
        # 3. CONTADOR DE GATOS (Felinos)
        cursor.execute("""
            SELECT COUNT(*) FROM Paciente p
            INNER JOIN Raza r ON p.CodigoRaza = r.CodigoRaza
            WHERE r.CodigoEspecie = 'FEL'
        """)
        total_gatos = cursor.fetchone()[0]
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error al leer base de datos o calcular estadísticas: {e}")
        todas_las_mascotas = []
        total_perros = 0
        total_gatos = 0
        
    return render_template('CitasP.html', 
                           mascotas=todas_las_mascotas, 
                           perros=total_perros, 
                           gatos=total_gatos)


# Corregido: Se quitó el doble @@ que rompía el inicio del servidor
@app.route('/citas-veterinario')
def citas_veterinario():
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        
        # Consulta corregida para usar únicamente los campos existentes en tu script SQL original
        cursor.execute("""
            SELECT 
                c.IdCita AS ID,
                c.FechaCita AS Fecha,
                p.NombreMacota AS Mascota,
                (per.Nombre + ' ' + per.Apellido) AS Dueño,
                c.Motivo AS Motivo
            FROM Cita c
            INNER JOIN Paciente p ON c.IdMacota = p.IdMacota
            LEFT JOIN Dueño d ON c.IdDueño = d.IdDueño  
            LEFT JOIN Persona per ON d.IdPersona = per.IdPersona
        """)
        todas_las_citas = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error al leer las citas de SQL Server: {e}")
        todas_las_citas = []
        
    return render_template('citasV.html', citas=todas_las_citas)


# --- 4. PROCESAR Y GUARDAR REGISTROS EN SQL SERVER ---

@app.route('/guardar-mascota', methods=['POST'])
def guardar_mascota():
    if request.method == 'POST':
        nombre_mascota = request.form['nombre_mascota']
        genero = request.form['genero']
        fecha_nacimiento = request.form['fecha_nacimiento']
        raza_texto = request.form['raza'] 
        peso = request.form['peso']

        conn = obtener_conexion()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT CodigoRaza FROM Raza WHERE NombreRaza = ?", (raza_texto,))
            resultado_raza = cursor.fetchone()
            
            codigo_raza = resultado_raza[0] if resultado_raza else 'MESC'
            
            query = """
                INSERT INTO Paciente (NombreMacota, Genero, FechaNacimiento, CodigoRaza, Peso)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (nombre_mascota, genero, fecha_nacimiento, codigo_raza, peso))
            conn.commit()
            
        except Exception as e:
            print(f"Error al registrar mascota: {e}")
        finally:
            cursor.close()
            conn.close()
            
        return redirect(url_for('citas_paciente'))


@app.route('/guardar-veterinario', methods=['POST'])
def guardar_veterinario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        telefono = request.form.get('telefono')
        email = request.form.get('email')
        especialidad = request.form.get('especialidad')

        conn = obtener_conexion()
        cursor = conn.cursor()
        
        try:
            # 1. Insertamos primero en Persona
            cursor.execute("""
                INSERT INTO Persona (Nombre, Apellido, Telefono, Email)
                VALUES (?, ?, ?, ?)
            """, (nombre, apellido, telefono, email))
            
            # 2. Capturamos el ID autogenerado
            cursor.execute("SELECT @@IDENTITY")
            id_persona = cursor.fetchone()[0]
            
            # 3. Insertamos en Veterinario usando ese ID
            cursor.execute("""
                INSERT INTO Veterinario (IdPersona, Especialidad)
                VALUES (?, ?)
            """, (id_persona, especialidad))
            
            conn.commit()
        except Exception as e:
            print(f"Hubo un error al registrar al veterinario: {e}")
        finally:
            cursor.close()
            conn.close()
            
        return redirect(url_for('inicio_sesion'))


# --- 5. LÓGICA DE INICIO DE SESIÓN (LOGIN) ---

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    tipo_usuario = request.form.get('tipo_usuario') 

    conn = obtener_conexion()
    cursor = conn.cursor()

    if tipo_usuario == 'veterinario':
        cursor.execute("""
            SELECT v.IdVeterinario 
            FROM Veterinario v
            INNER JOIN Persona p ON v.IdPersona = p.IdPersona
            WHERE p.Email = ?
        """, (email,))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        if usuario:
            return redirect(url_for('citas_veterinario'))
            
    elif tipo_usuario == 'paciente':
        cursor.execute("""
            SELECT d.IdDueño 
            FROM Dueño d
            INNER JOIN Persona p ON d.IdPersona = p.IdPersona
            WHERE p.Email = ?
        """, (email,))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        if usuario:
            return redirect(url_for('citas_paciente'))

    return "Correo o tipo de usuario incorrectos. <a href='/login-seleccion'>Volver a intentar</a>"


if __name__ == '__main__':
    app.run(debug=True)