import mysql.connector

# CONEXION CON LA BASE DE DATOS
cnx = mysql.connector.connect(
    host='localhost',
    user='natcord',
    password='123',
    database='pruebapos')

# CURSOR PARA EJECUTAR LAS CONSULTAS
cursor = cnx.cursor()

"""# Definir la sentencia SQL para crear la tabla"""
sql = """
CREATE TABLE tu_tabla (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT,
    correo VARCHAR(100)
)"""

# INSERTAR DATOS DENTRO EN LA BASE DE DATOS
"""sql = "INSERT INTO tu_tabla (id, nombre, edad, correo) VALUES (%s,%s,%s,%s)"
datos=(1,"Nataly", 23, "soporte3@dinivalsas.com")
cursor.execute(sql, datos)"""

# VISUALIZAR DATOS EN LA BASE DE DATOS
"""sql = "SELECT * FROM tu_tabla"
cursor.execute(sql)              # Ejecutar la sentencia SQL
results = cursor.fetchall()
for row in results:
    print(row)"""
    
# VISUALIZAR UNA COLUMNA EN LA BASE DE DATOS
"""sql = "SELECT correo FROM tu_tabla"
cursor.execute(sql)              # Ejecutar la sentencia SQL
results = cursor.fetchall()
for row in results:
    print(row)"""

# AGREGAR UNA NUEVA COLUMNA EN LA BASE DE DATOS
"""sql = "ALTER TABLE tu_tabla ADD departamento VARCHAR(50)"
cursor.execute(sql)"""

# CONSULTAR UN DATO Y AGREGARLE EN LA COLUMNA CORRESPONDIENTE INFORMACIÓN 
sql = """UPDATE tu_tabla 
SET departamento = 'procesamiento'
WHERE nombre = 'Nataly' 
cursor.execute(sql)   """

# CONFIRMAR DATOS EN LA BASE DE DATOS
cnx.commit()

# Cerrar el cursor y la conexión
cursor.close()
cnx.close()