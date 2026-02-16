import xmlrpc.client

def get_odoo_connection():
    url = 'https://vise.avancyserp.com'  # Cambia esto por la URL de tu instancia de Odoo
    db = 'vise' # Cambia esto por el nombre de tu base de datos
    username = 'agiraldo@vise.com.co'  # Cambia esto por tu usuario
    password = 'edd4236354419bbb877fb58d8ad6c44465b44ed5'  # Cambia esto por tu contraseña

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    return models, uid, password, db

def migrate_data():
    models, uid, password, db = get_odoo_connection()
    modelo = 'note.note'

    campos = {
        'memo': 'Holas',
    }

    record_id = models.execute_kw(db, uid, password, modelo, 'create', [campos])

migrate_data()
