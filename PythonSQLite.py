import sqlite3

# Conexion
conexion = sqlite3.connect('universidad.db')

try:
    cursor = conexion.cursor()

    # Estructura
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tabla_01 (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            UsuarioNombre TEXT,
            UsuarioApellido TEXT,
            UsuarioPais TEXT
        )
    """)

    # (INSERT)
    sql = "INSERT INTO tabla_01 (UsuarioNombre, UsuarioApellido, UsuarioPais) VALUES (?, ?, ?)"
    cursor.execute(sql, ("Alan", "Turing", "Reino Unido"))
    
    # Commit
    conexion.commit()
    print("¡Datos guardados con éxito en el archivo .db!")

finally:
    # Cerrar Conexion
    conexion.close()