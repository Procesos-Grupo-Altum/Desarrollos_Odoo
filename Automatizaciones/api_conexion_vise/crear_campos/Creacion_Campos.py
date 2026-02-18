from Api_conexion import odoo_env

# --- Variables de conexión ---
url = odoo_env["url"]
db = odoo_env["db"]
uid = odoo_env["uid"]
password = odoo_env["password"]
models = odoo_env["models"]


# Lista de campos a crear
CAMPOS = [
    # {"name": "x_order", "field_description": "Campo Orden", "ttype": "boolean"},
    # {"name": "x_date_field_id", "field_description": "Campo Fecha", "ttype": "many2one", "relation": "ir.model.fields", "required": False, "store": True,}
    {"name": "x_adjunto_field_id", "field_description": "Adjunto", "ttype": "many2one", "relation": "ir.model.fields", "required": False, "store": True,},
    # {"name": "x_fecha_referencia", "field_description": "Fecha Referencia", "related": "x_adjunto_field_id.valid_from", "ttype": "date", "required": False, "readonly": False, "store": True,},
]

def crear_campos(modelo, campos):
    """Crea múltiples campos en el modelo dado."""
    # Obtener ID del modelo
    model_id = models.execute_kw(
        db, uid, password,
        "ir.model", "search",
        [[["model", "=", modelo]]],
        {"limit": 1}
    )
    if not model_id:
        print(f"❌ Modelo '{modelo}' no encontrado.")
        return

    model_id = model_id[0]

    for campo in campos:
        # Verificar si ya existe
        existe = models.execute_kw(
            db, uid, password,
            "ir.model.fields", "search",
            [[["model", "=", modelo], ["name", "=", campo["name"]]]]
        )
        if existe:
            print(f"⚠️ El campo '{campo['name']}' ya existe en '{modelo}'.")
            continue

        # Crear campo
        field_id = models.execute_kw(
            db, uid, password,
            "ir.model.fields", "create",
            [{
                "name": campo["name"],
                "field_description": campo["field_description"],
                "ttype": campo["ttype"],
                "model_id": model_id,
                "relation": campo.get("relation"),
                "required": campo.get("required", False),
                "state": "manual",
                "store": True,       # necesario en Odoo 16+
                "readonly": False,
            }]
        )
        print(f"✅ Campo '{campo['name']}' creado con ID {field_id}.")


def eliminar_campos(modelo, campos):
    """Elimina múltiples campos en el modelo dado."""
    for campo in campos:
        field_ids = models.execute_kw(
            db, uid, password,
            "ir.model.fields", "search",
            [[["model", "=", modelo], ["name", "=", campo["name"]]]]
        )

        if not field_ids:
            print(f"⚠️ El campo '{campo['name']}' no existe en '{modelo}'.")
            continue

        models.execute_kw(
            db, uid, password,
            "ir.model.fields", "unlink",
            [field_ids]
        )
        print(f"🗑️ Campo '{campo['name']}' eliminado de '{modelo}'.")


if __name__ == "__main__":
    modelo = "gestion.trd"  # puedes cambiar el modelo aquí
    # modelo = "x_relacion.trd"  # puedes cambiar el modelo aquí

    print("👉 Creando campos...")
    crear_campos(modelo, CAMPOS)

    # Descomenta si quieres probar eliminación
    #print("👉 Eliminando campos...")
    #eliminar_campos(modelo, CAMPOS)
