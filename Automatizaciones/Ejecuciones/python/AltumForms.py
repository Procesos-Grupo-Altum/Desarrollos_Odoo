import mysql.connector

# Establecer la conexión
conexion = mysql.connector.connect(
    host="35.227.100.201",
    user="altumformsconsulta",
    password="4ltumF0rms.$2021",
    database="forms_altum_hist"
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Ejecutar una consulta
cursor.execute("SELECT question_answer_id, question_answer_group_id, question_id, question_option_id, replace(value,'/','') FROM forms_altum_hist.question_answer limit 100000;")

# Obtener los resultados
resultados = cursor.fetchall()

# Imprimir los resultados
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
