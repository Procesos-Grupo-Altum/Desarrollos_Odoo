import xmlrpc.client
from Api_conexion import odoo_env

url = odoo_env["url"]
db = odoo_env["db"]
uid = odoo_env["uid"]
password = odoo_env["password"]
models = odoo_env["models"]

def crear_campo_many2many_movimientos():
    try:
        modelo_prueba_ids = models.execute_kw(
            db, uid, password,
            'ir.model', 'search',
            [[['model', '=', 'x_mi_modelo_prueba']]]
        )
        if not modelo_prueba_ids:
            raise Exception("No se encontró el modelo x_mi_modelo_prueba")

        modelo_prueba_id = modelo_prueba_ids[0]

        campo_id = models.execute_kw(
            db, uid, password,
            'ir.model.fields', 'create',
            [{
                'model_id': modelo_prueba_id,
                'name': 'x_movimientos_contables_ids',
                'field_description': 'Movimientos contables (líneas)',
                'ttype': 'many2many',
                'relation': 'account.move.line',
                'relation_table': 'x_account_move_line_x_mi_modelo_prueba_rel',
                'column1': 'x_mi_modelo_prueba_id',
                'column2': 'account_move_line_id',
            }]
        )
        print(f"✅ Campo creado (ID: {campo_id}).")
        return campo_id

    except Exception as e:
        print(f"❌ Error al crear el campo: {e}")
        return None

crear_campo_many2many_movimientos()
