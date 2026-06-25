from flask import Flask, render_template, request, redirect, url_for
import pyodbc 

app = Flask(__name__)

# --- 1. CONFIGURACIÓN DE CONEXIÓN A SQL SERVER ---
SERVIDOR = '(localdb)\\MSSQLLocalDB'  
BASE_DATOS = 'VetConnet'  # Apuntando a tu BD de la función de conexión

def obtener_conexion():
    return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\\MSSQLLocalDB;DATABASE=VetConnet;Trusted_Connection=yes;')


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



@app.route('/citas-veterinario')
def citas_veterinario():
    todas_las_citas = []
    lista_mascotas = []
    
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        
        # 1. TABLA DE CITAS BLINDADA (Muestra TODO lo que haya en SSMS aunque falten datos)
        try:
            cursor.execute("""
    SELECT 
        c.IdCita AS ID,
        CONVERT(varchar(10), c.FechaCita, 103) AS Fecha,
        CONVERT(varchar(5), c.FechaCita, 108) AS Hora,
        ISNULL(p.NombreMacota, 'Mascota No Asignada') AS Mascota,
        ISNULL(per.Nombre + ' ' + per.Apellido, 'Sin Dueño') AS Dueño,
        c.Motivo AS Motivo,
        ISNULL(c.Estado, 'Pendiente') AS Estado
    FROM Cita c
    LEFT JOIN Paciente p ON c.IdMacota = p.IdMacota
    LEFT JOIN Dueño d ON c.IdDueño = d.IdDueño
    LEFT JOIN Persona per ON d.IdPersona = per.IdPersona
    ORDER BY c.FechaCita DESC
""")
            todas_las_citas = cursor.fetchall()
        except Exception as e_citas:
            print(f" Error al leer tabla Citas: {e_citas}")

        # 2. SELECTOR DEL MODAL (Se mantiene funcionando e independiente)
        try:
            cursor.execute("SELECT IdMacota, NombreMacota FROM Paciente")
            filas = cursor.fetchall()
            for f in filas:
                lista_mascotas.append((f[0], f[1], "Dueño de la Base de Datos"))
        except Exception as e_mascotas:
            print(f" Error al leer tabla Paciente: {e_mascotas}")
            
        cursor.close()
        conn.close()
        
    except Exception as e_global:
        print(f" Error general de conexión: {e_global}")

    # Plan B por si la tabla de pacientes está vacía en tu entorno local
    if not lista_mascotas:
        lista_mascotas = [
            (12, "Sofi (Respaldo)", "Maria"),
            (15, "Toby (Respaldo)", "Juan Carlos")
        ]
        
    return render_template('citasV.html', citas=todas_las_citas, lista_mascotas=lista_mascotas)



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


# 🌟 ACTUALIZAR PACIENTE DESDE MODAL EDITAR
@app.route('/editar-mascota', methods=['POST'])
def editar_mascota():
    codigo = request.form.get('codigo')
    nombre = request.form.get('nombre_mascota')
    genero = request.form.get('genero')
    fecha = request.form.get('fecha_nacimiento')
    peso = request.form.get('peso')

    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Paciente 
            SET NombreMacota = ?, Genero = ?, FechaNacimiento = ?, Peso = ? 
            WHERE IdMacota = ?
        """, (nombre, genero, fecha, peso, codigo))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error al actualizar la mascota {codigo}: {e}")

    return redirect(url_for('citas_paciente'))


# 🌟 GUARDAR DIAGNÓSTICO DESDE EL MODAL DIAGNÓSTICO
@app.route('/guardar-diagnostico', methods=['POST'])
def guardar_diagnostico():
    codigo_mascota = request.form.get('codigo_mascota')
    descripcion = request.form.get('descripcion')
    treatment = request.form.get('tratamiento')

    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Diagnostico (IdMacota, Descripcion, Tratamiento) 
            VALUES (?, ?, ?)
        """, (codigo_mascota, descripcion, treatment))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error al guardar diagnóstico para {codigo_mascota}: {e}")

    return redirect(url_for('citas_paciente'))


# ELIMINAR PACIENTE
@app.route('/eliminar-mascota/<int:codigo>', methods=['POST', 'GET'])
def eliminar_mascota(codigo):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Paciente WHERE IdMacota = ?", (codigo,))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error al eliminar la mascota {codigo}: {e}")

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
            cursor.execute("""
                INSERT INTO Persona (Nombre, Apellido, Telefono, Email)
                VALUES (?, ?, ?, ?)
            """, (nombre, apellido, telefono, email))
            
            cursor.execute("SELECT @@IDENTITY")
            id_persona = cursor.fetchone()[0]
            
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


#  RUTA PARA GUARDAR LA CITA CONFIGURADA CON EL SELECTOR AUTOMÁTICO
#  RUTA PARA GUARDAR LA CITA MEJORADA
@app.route('/guardar-cita', methods=['POST'])
def guardar_cita():
    fecha = request.form.get('fecha_cita')
    hora = request.form.get('hora_cita')
    codigo_mascota = request.form.get('codigo_mascota')
    motivo = request.form.get('motivo')
    estado = request.form.get('estado') or 'Pendiente'

    print("\n--- DATOS RECIBIDOS DEL FORMULARIO HTML ---")
    print(request.form)

    if not fecha or not hora or not codigo_mascota or not motivo:
        return "Error: faltan datos del formulario de cita.", 400

    fecha_completa = f"{fecha} {hora}:00"

    try:
        conn = obtener_conexion()
        cursor = conn.cursor()

        query = """
            INSERT INTO Cita (IdMacota, FechaCita, Motivo, Estado)
            VALUES (?, ?, ?, ?)
        """

        cursor.execute(query, (codigo_mascota, fecha_completa, motivo, estado))
        conn.commit()

        print("Cita guardada correctamente en SQL Server.")

    except Exception as e:
        print(f"Error al guardar cita: {e}")
        return f"Error en la base de datos: {e}", 500

    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('citas_veterinario'))

@app.route('/actualizar-estado-cita/<int:id_cita>', methods=['POST'])
def actualizar_estado_cita(id_cita):
    nuevo_estado = request.form.get('estado')

    try:
        conn = obtener_conexion()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Cita
            SET Estado = ?
            WHERE IdCita = ?
        """, (nuevo_estado, id_cita))

        conn.commit()
        cursor.close()
        conn.close()

        return "Estado actualizado correctamente", 200

    except Exception as e:
        print(f"Error al actualizar estado de cita: {e}")
        return f"Error al actualizar estado: {e}", 500



    

   


    


if __name__ == '__main__':
    app.run(debug=True)