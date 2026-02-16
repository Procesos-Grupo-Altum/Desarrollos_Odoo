import mysql.connector
import xmlrpc.client
import html

# Configuración de la conexión a MySQL
def get_mysql_connection():
    return mysql.connector.connect(
        host="34.148.152.58",
        user="altumformsconsulta",
        password="D5JqhfxiPi1yOeafPgwL",
        database="forms_altum_hist"
    )

# Configuración de la conexión a Odoo
def get_odoo_connection():
    url = 'https://altumforms2.odoo.com'  # Cambia esto por la URL de tu instancia de Odoo
    db = 'altumforms2'  # Cambia esto por el nombre de tu base de datos
    username = 'procesos@grupoaltum.com.co'  # Cambia esto por tu usuario
    password = 'a3fba95d1eae9af06fd1ae50169254c09831ce81'  # Cambia esto por tu contraseña

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    return models, uid, password, db

def replace(text, chars):
    if text is None:
        return ""
    for char in chars:
        text = text.replace(char, "")
    return text

def clean_xml_invalid_chars(text):
    if not text:
        return text
    # Elimina caracteres inválidos en XML (como \x00)
    return ''.join(char for char in text if ord(char) > 31 or char in '\n\r\t')

# Obtener el último ID de Odoo
def get_last_odoo_id(models, uid, password, db, model):
    # Obtener el ID del último registro
    last_ids = models.execute_kw(db, uid, password, model, 'search', [[]], {'limit': 1, 'order': 'x_name desc'})
    if not last_ids:
        return 0

    # Obtener los detalles del último registro
    last_record = models.execute_kw(db, uid, password, model, 'read', [last_ids[0]])
    if last_record:
        print(last_record[0]['x_name'])  # Imprimir el valor de x_name del último registro

    return last_record[0]['x_name']


# Consultar datos de MySQL
def fetch_mysql_data(last_id):
    # print(last_id)
    connection = get_mysql_connection()
    cursor = connection.cursor()


    query = (f"SELECT question_answer_id, question_answer_group_id, question_id, question_option_id, replace(replace(value,'',''),'/','') FROM forms_altum.question_answer WHERE question_answer_id > {last_id} LIMIT 100000"
             f"")
    cursor.execute(query)
    results = cursor.fetchall()
    # cursor.close()
    # connection.close()
    # print(results)
    return results

# Insertar datos en Odoo
def insert_data_into_odoo(models, uid, password, db, model, data):
    records=[]
    for row in data:
        valor = replace(row[4], ['\\', '/'])  # Elimina '\' y '/'
        valor = clean_xml_invalid_chars(valor)  # Limpia caracteres inválidos en XML
        valor = html.escape(valor) if valor else ""  # Escapa caracteres especiales
        # print(valor)

        record = {


            'x_name': row[0],
            'x_registro': row[1],
            'x_pregunta': row[2],
            'x_pregunta_opcion': row[3] if row[3] is not None else "",
            'x_valor': valor if valor is not None else "",
        }








































        records.append(record)
    return records

# Función principal para realizar la migración
def migrate_data():
    models, uid, password, db = get_odoo_connection()
    model = 'x_respuestas'
    last_id = get_last_odoo_id(models, uid, password, db, model)
    data = fetch_mysql_data(last_id)
    data2=insert_data_into_odoo(models, uid, password, db, model, data)
    print(data2[0])
    print(len(data2))
    record_id = models.execute_kw(db, uid, password, model, 'create', [data2])

migrate_data()
