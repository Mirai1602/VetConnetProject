from flask import Flask, render_template, request, redirect, url_for, jsonify
import pyodbc 

app = Flask(__name__)

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

        # Trae pacientes con nombre del dueño incluido
        cursor.execute("""
     SELECT
    p.IdMacota AS Codigo,
    p.NombreMacota AS Mascota,
    ISNULL(per.Nombre + ' ' + per.Apellido, 'Sin Dueño Asignado') AS Dueño,
    r.NombreRaza AS Raza,
    p.FechaNacimiento AS [F. Nacimiento],
    p.Genero AS Género,
    p.Peso AS Peso,
    e.NombreEspecie AS Especie,
    ISNULL(NULLIF(per.Telefono, ''), 'No registrado') AS Telefono,
    ISNULL(NULLIF(d.Direccion, ''), 'No registrada') AS Direccion,
    ISNULL(NULLIF(per.Email, ''), 'No registrado') AS Correo
FROM Paciente p
INNER JOIN Raza r ON p.CodigoRaza = r.CodigoRaza
INNER JOIN Especie e ON r.CodigoEspecie = e.CodigoEspecie
LEFT JOIN Dueño d ON p.IdMacota = d.IdMacota
LEFT JOIN Persona per ON d.IdPersona = per.IdPersona

""")
        todas_las_mascotas = cursor.fetchall()

        cursor.execute("""
            SELECT COUNT(*) FROM Paciente p
            INNER JOIN Raza r ON p.CodigoRaza = r.CodigoRaza
            WHERE r.CodigoEspecie = 'CAN'
        """)
        total_perros = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*) FROM Paciente p
            INNER JOIN Raza r ON p.CodigoRaza = r.CodigoRaza
            WHERE r.CodigoEspecie = 'FEL'
        """)
        total_gatos = cursor.fetchone()[0]

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error al leer base de datos: {e}")
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
            """)
            todas_las_citas = cursor.fetchall()
        except Exception as e_citas:
            print(f" Error al leer tabla Citas: {e_citas}")

        try:
            cursor.execute("SELECT IdMacota, NombreMacota FROM Paciente")
            filas = cursor.fetchall()
            if filas:
                for f in filas:
                    lista_mascotas.append((f[0], f[1], "Dueño de la Base de Datos"))
        except Exception as e_mascotas:
            print(f" Error al leer pacientes: {e_mascotas}")

        cursor.close()
        conn.close()

    except Exception as e_global:
        print(f" Error general de conexión: {e_global}")

    if not lista_mascotas:
        lista_mascotas = [
            (12, "Sofi (Respaldo)", "Maria"),
            (15, "Toby (Respaldo)", "Juan Carlos")
        ]

    cont_pendientes = sum(1 for cita in todas_las_citas if cita[6] == 'Pendiente')
    cont_hechas = sum(1 for cita in todas_las_citas if cita[6] == 'Hecha')

    return render_template('citasV.html',
                           citas=todas_las_citas,
                           lista_mascotas=lista_mascotas,
                           num_p=cont_pendientes,
                           num_h=cont_hechas)


@app.route('/guardar-mascota', methods=['POST'])
def guardar_mascota():
    # Datos de la mascota
    nombre_mascota   = request.form.get('nombre_mascota')
    genero           = request.form.get('genero')
    fecha_nacimiento = request.form.get('fecha_nacimiento')
    raza_texto       = request.form.get('raza')
    peso             = request.form.get('peso')

    # Datos del dueño
    nombre_dueno     = request.form.get('dueno', '').strip()
    telefono         = request.form.get('telefono', '').strip()
    direccion        = request.form.get('direccion', '').strip()
    correo           = request.form.get('correo', '').strip()

    conn = obtener_conexion()
    cursor = conn.cursor()

    try:
        # Buscar CodigoRaza
        cursor.execute("SELECT CodigoRaza FROM Raza WHERE NombreRaza = ?", (raza_texto,))
        resultado_raza = cursor.fetchone()
        codigo_raza = resultado_raza[0] if resultado_raza else 'MESC'

        # Insertar paciente
        cursor.execute("""
            INSERT INTO Paciente (NombreMacota, Genero, FechaNacimiento, CodigoRaza, Peso)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre_mascota, genero, fecha_nacimiento, codigo_raza, peso))

        # Obtener el ID recién insertado
        cursor.execute("SELECT @@IDENTITY")
        id_mascota = int(cursor.fetchone()[0])

        # Si viene nombre de dueño, registrar Persona + Dueño
        if nombre_dueno:
            partes = nombre_dueno.split(' ', 1)
            nombre   = partes[0]
            apellido = partes[1] if len(partes) > 1 else ''

            # Insertar persona con teléfono y correo
            cursor.execute("""
                INSERT INTO Persona (Nombre, Apellido, Telefono, Email)
                VALUES (?, ?, ?, ?)
            """, (nombre, apellido, telefono, correo))

            cursor.execute("SELECT @@IDENTITY")
            id_persona = int(cursor.fetchone()[0])

            # Insertar dueño con dirección y relación a mascota
            cursor.execute("""
                INSERT INTO Dueño (IdPersona, Direccion, IdMacota)
                VALUES (?, ?, ?)
            """, (id_persona, direccion, id_mascota))

        conn.commit()

    except Exception as e:
        print(f"Error al registrar mascota: {e}")
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('citas_paciente'))





@app.route('/editar-mascota', methods=['POST'])
def editar_mascota():
    codigo  = request.form.get('codigo')
    nombre  = request.form.get('nombre_mascota')
    genero  = request.form.get('genero')
    fecha   = request.form.get('fecha_nacimiento')
    peso    = request.form.get('peso')
    nombre_dueno = request.form.get('dueno', '').strip()
    telefono     = request.form.get('telefono', '').strip()
    correo       = request.form.get('correo', '').strip()
    direccion    = request.form.get('direccion', '').strip()

    try:
        conn = obtener_conexion()
        cursor = conn.cursor()

        # Actualizar paciente
        cursor.execute("""
            UPDATE Paciente 
            SET NombreMacota = ?, Genero = ?, FechaNacimiento = ?, Peso = ? 
            WHERE IdMacota = ?
        """, (nombre, genero, fecha, peso, codigo))

        # Actualizar o crear dueño si viene el nombre
        if nombre_dueno:
            partes   = nombre_dueno.split(' ', 1)
            pnombre  = partes[0]
            papellido = partes[1] if len(partes) > 1 else ''

            # ¿Ya tiene dueño este paciente?
            cursor.execute("SELECT d.IdDueño, d.IdPersona FROM Dueño d WHERE d.IdMacota = ?", (codigo,))
            dueno_existente = cursor.fetchone()

            if dueno_existente:
                # Actualizar Persona existente (nombre, teléfono y correo)
                cursor.execute("""
                    UPDATE Persona SET Nombre = ?, Apellido = ?, Telefono = ?, Email = ?
                    WHERE IdPersona = ?
                """, (pnombre, papellido, telefono, correo, dueno_existente[1]))

                # Actualizar dirección en el registro de Dueño
                cursor.execute("""
                    UPDATE Dueño SET Direccion = ?
                    WHERE IdDueño = ?
                """, (direccion, dueno_existente[0]))
            else:
                # Crear nueva Persona con teléfono y correo
                cursor.execute("""
                    INSERT INTO Persona (Nombre, Apellido, Telefono, Email)
                    VALUES (?, ?, ?, ?)
                """, (pnombre, papellido, telefono, correo))
                cursor.execute("SELECT @@IDENTITY")
                id_persona = int(cursor.fetchone()[0])

                # Crear Dueño con dirección
                cursor.execute("""
                    INSERT INTO Dueño (IdPersona, Direccion, IdMacota) VALUES (?, ?, ?)
                """, (id_persona, direccion, codigo))

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error al actualizar la mascota {codigo}: {e}")

    return redirect(url_for('citas_paciente'))

@app.route('/guardar-diagnostico', methods=['POST'])
def guardar_diagnostico():
    codigo_mascota = request.form.get('codigo_mascota')
    descripcion    = request.form.get('descripcion')
    treatment      = request.form.get('tratamiento')

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
        return redirect(url_for('citas_paciente', guardado='true'))
    except Exception as e:
        print(f"Error al guardar diagnóstico: {e}")
        return redirect(url_for('citas_paciente', error='true'))

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


@app.route('/historial-diagnosticos/<int:id_mascota>', methods=['GET'])
def historial_diagnosticos(id_mascota):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        
        # Buscamos todos los diagnósticos de esta mascota en específico
        cursor.execute("""
            SELECT IdDiagnostico, Descripcion, Tratamiento 
            FROM Diagnostico 
            WHERE IdMacota = ? 
            ORDER BY IdDiagnostico DESC
        """, (id_mascota,))
        
        filas = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # Convertimos las filas a una lista de diccionarios para enviarla a JavaScript
        lista_historial = []
        for f in filas:
            lista_historial.append({
                "id": f[0],
                "descripcion": f[1],
                "tratamiento": f[2]
            })
            
        return jsonify({"status": "success", "historial": lista_historial}), 200
    except Exception as e:
        print(f" Error al consultar historial: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/guardar-veterinario', methods=['POST'])
def guardar_veterinario():
    nombre      = request.form.get('nombre')
    apellido    = request.form.get('apellido')
    telefono    = request.form.get('telefono')
    email       = request.form.get('email')
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
            INSERT INTO Veterinario (IdPersona, Especialidad) VALUES (?, ?)
        """, (id_persona, especialidad))
        conn.commit()
    except Exception as e:
        print(f"Error al registrar veterinario: {e}")
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('inicio_sesion'))


@app.route('/login', methods=['POST'])
def login():
    email        = request.form.get('email')
    tipo_usuario = request.form.get('tipo_usuario')

    conn = obtener_conexion()
    cursor = conn.cursor()

    if tipo_usuario == 'veterinario':
        cursor.execute("""
            SELECT v.IdVeterinario FROM Veterinario v
            INNER JOIN Persona p ON v.IdPersona = p.IdPersona
            WHERE p.Email = ?
        """, (email,))
        usuario = cursor.fetchone()
        cursor.close(); conn.close()
        if usuario:
            return redirect(url_for('citas_veterinario'))

    elif tipo_usuario == 'paciente':
        cursor.execute("""
            SELECT d.IdDueño FROM Dueño d
            INNER JOIN Persona p ON d.IdPersona = p.IdPersona
            WHERE p.Email = ?
        """, (email,))
        usuario = cursor.fetchone()
        cursor.close(); conn.close()
        if usuario:
            return redirect(url_for('citas_paciente'))

    return "Correo o tipo de usuario incorrectos. <a href='/login-seleccion'>Volver a intentar</a>"


@app.route('/guardar-cita', methods=['POST'])
def guardar_cita():
    fecha          = request.form.get('fecha_cita')
    hora           = request.form.get('hora_cita')
    codigo_mascota = request.form.get('codigo_mascota')
    motivo         = request.form.get('motivo')
    estado         = request.form.get('estado') or 'Pendiente'

    if not fecha or not hora or not codigo_mascota or not motivo:
        return "Error: faltan datos del formulario de cita.", 400

    fecha_completa = f"{fecha} {hora}:00"

    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Cita (IdMacota, FechaCita, Motivo, Estado)
            VALUES (?, ?, ?, ?)
        """, (codigo_mascota, fecha_completa, motivo, estado))
        conn.commit()
    except Exception as e:
        print(f"Error al guardar cita: {e}")
        return f"Error en la base de datos: {e}", 500
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('citas_veterinario'))


@app.route('/actualizar-estado-cita', methods=['POST'])
def actualizar_estado_cita():
    try:
        datos       = request.get_json()
        id_cita     = datos.get('id_cita')
        nuevo_estado = datos.get('estado')

        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("UPDATE Cita SET Estado = ? WHERE IdCita = ?", (nuevo_estado, id_cita))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"status": "success", "message": "Estado actualizado en la BD"}), 200
    except Exception as e:
        print(f"Error al actualizar estado: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)