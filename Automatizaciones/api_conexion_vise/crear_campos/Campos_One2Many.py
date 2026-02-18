from Api_conexion import odoo_env  # Importamos la conexión desde tu archivo

# --- Variables de conexión ---
url = odoo_env["url"]
db = odoo_env["db"]
uid = odoo_env["uid"]
password = odoo_env["password"]
models = odoo_env["models"]

def crear_campo_one2many(nombre_campo, etiqueta, modelo_relacionado, campo_inverso):
    try:
        # Obtener el ID del modelo x_mi_modelo_prueba
        modelo_prueba_id = models.execute_kw(
            db, uid, password,
            'ir.model', 'search',
            [[['model', '=', 'x_mi_modelo_prueba']]]
        )[0]

        # Crear el campo One2many en x_mi_modelo_prueba
        campo_id = models.execute_kw(
            db, uid, password,
            'ir.model.fields', 'create',
            [{
                'model_id': modelo_prueba_id,
                'name': nombre_campo,
                'field_description': etiqueta,
                'ttype': 'one2many',
                'relation': modelo_relacionado,
                'relation_field': campo_inverso,
            }]
        )
        print(f"✅ Campo '{nombre_campo}' creado con éxito en x_mi_modelo_prueba (ID: {campo_id}).")
        return campo_id
    except Exception as e:
        print(f"❌ Error al crear el campo: {e}")
        return None

# Crear el campo One2many en x_mi_modelo_prueba
crear_campo_one2many(
    nombre_campo='x_contratos',
    etiqueta='Contratos Asociados',
    modelo_relacionado='hr.contract',
    campo_inverso='x_mi_modelo_prueba_id'
)
