import pymysql

# pip install pymysql
# Parametros de conexion
db = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='pythontest'
)

try:
    cursor = db.cursor()

    # (INSERT)
    sql_insert = "INSERT INTO tabla_01 (UsuarioNombre, UsuarioApellido, UsuarioPais) VALUES (%s, %s, %s)"
    cursor.execute(sql_insert, ("Alan", "Turing", "Reino Unido"))
    db.commit()
    print("Registro guardado con exito.")

    # # (SELECT)
    # cursor.execute("SELECT * FROM tabla_01")
    # resultados = cursor.fetchall()

    # for fila in resultados:
    #     print(fila)

finally:
    # Cerrar conexion
    db.close()