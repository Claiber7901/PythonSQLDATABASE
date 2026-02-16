import sqlite3

# 1. Conexión (Crea el archivo si no existe, no necesita XAMPP)
conexion = sqlite3.connect('universidad.db')

try:
    cursor = conexion.cursor()

    # 2. Estructura (Creamos la tabla si es la primera vez que corre)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tabla_01 (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            UsuarioNombre TEXT,
            UsuarioApellido TEXT,
            UsuarioPais TEXT
        )
    """)

    # 3. Mandar información (Insertar)
    sql = "INSERT INTO tabla_01 (UsuarioNombre, UsuarioApellido, UsuarioPais) VALUES (?, ?, ?)"
    cursor.execute(sql, ("Alan", "Turing", "Reino Unido"))
    
    # 4. Guardar y confirmar
    conexion.commit()
    print("¡Datos guardados con éxito en el archivo .db!")

finally:
    # 5. Cerrar el puente
    conexion.close()