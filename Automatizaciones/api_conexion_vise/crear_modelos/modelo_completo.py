from Api_conexion import odoo_env  # Importamos la conexión desde tu archivo

# --- Variables de conexión ---
url = odoo_env["url"]
db = odoo_env["db"]
uid = odoo_env["uid"]
password = odoo_env["password"]
models = odoo_env["models"]

# ----------------------------
# Helpers
# ----------------------------
def search_one(model, domain, fields=None):
    """Devuelve (id, data_dict) del primer registro que cumpla domain."""
    ids = models.execute_kw(db, uid, password, model, "search", [domain], {"limit": 1})
    if not ids:
        return None, None
    rid = ids[0]
    if fields:
        data = models.execute_kw(db, uid, password, model, "read", [[rid], fields])[0]
        return rid, data
    return rid, None

# --- Función para crear un modelo personalizado ---
def crear_modelo(nombre_modelo, nombre_descriptivo):
    """
    Crea un modelo personalizado en Odoo.

    :param nombre_modelo: Nombre técnico del modelo (ej: 'x_custom_model')
    :param nombre_descriptivo: Nombre descriptivo del modelo (ej: 'Modelo Personalizado')
    :return: ID del modelo creado
    """
    try:
        # Verificar si el modelo ya existe
        modelo_id = models.execute_kw(
            db, uid, password,
            'ir.model', 'search',
            [[['model', '=', nombre_modelo]]]
        )
        if modelo_id:
            print(f"⚠️ El modelo '{nombre_modelo}' ya existe (ID: {modelo_id[0]}).")
            return modelo_id[0]

        # Crear el modelo
        modelo_id = models.execute_kw(
            db, uid, password,
            'ir.model', 'create',
            [{
                'model': nombre_modelo,
                'name': nombre_descriptivo,
                'state': 'manual',  # Indica que es un modelo personalizado
                'transient': False,  # Quitar si no es necesario
            }]
        )
        print(f"✅ Modelo '{nombre_modelo}' creado con éxito (ID: {modelo_id}).")
        return modelo_id
    except Exception as e:
        print(f"❌ Error al crear el modelo: {e}")
        return None


# --- Función para crear campos en un modelo ---
def crear_campo(modelo_id, nombre_campo, tipo_campo, etiqueta, **kwargs):
    """
    Crea un campo en un modelo existente.

    :param modelo_id: ID del modelo (ir.model)
    :param nombre_campo: Nombre técnico del campo (ej: 'x_nombre_campo')
    :param tipo_campo: Tipo de campo (ej: 'char', 'integer', 'many2one', etc.)
    :param etiqueta: Etiqueta del campo (ej: 'Nombre del Campo')
    :param kwargs: Argumentos adicionales (ej: required=True, relation='res.partner')
    :return: ID del campo creado
    """
    try:
        # Verificar si el campo ya existe
        campo_id = models.execute_kw(
            db, uid, password,
            'ir.model.fields', 'search',
            [[['model_id', '=', modelo_id], ['name', '=', nombre_campo]]]
        )
        if campo_id:
            print(f"⚠️ El campo '{nombre_campo}' ya existe (ID: {campo_id[0]}).")
            return campo_id[0]

        # Crear el campo
        campo_id = models.execute_kw(
            db, uid, password,
            'ir.model.fields', 'create',
            [{
                'model_id': modelo_id,
                'name': nombre_campo,
                'field_description': etiqueta,
                'ttype': tipo_campo,
                **kwargs,
            }]
        )
        print(f"✅ Campo '{nombre_campo}' creado con éxito (ID: {campo_id}).")
        return campo_id
    except Exception as e:
        print(f"❌ Error al crear el campo: {e}")
        return None

def actualizar_campo_related(modelo_id, nombre_campo, related_path, store=True, readonly=True):
    """
    Actualiza un campo existente para que sea related (ej: x_nombre.name).
    """
    try:
        field_id, data = search_one(
            "ir.model.fields",
            [["model_id", "=", modelo_id], ["name", "=", nombre_campo]],
            fields=["id", "name", "ttype", "related"]
        )
        if not field_id:
            print(f"❌ No existe el campo '{nombre_campo}' para actualizar.")
            return None

        # Recomendación: related a Char debe ser ttype 'char'
        ttype = data.get("ttype")
        if ttype != "char":
            print(f"⚠️ Aviso: '{nombre_campo}' es ttype='{ttype}'. Un related a texto normalmente debe ser 'char'.")

        ok = models.execute_kw(
            db, uid, password,
            "ir.model.fields", "write",
            [[field_id], {
                "related": related_path,
                "store": bool(store),
                "readonly": bool(readonly),
            }]
        )
        print(f"✅ Campo '{nombre_campo}' actualizado como related='{related_path}'. Resultado write: {ok} (ID: {field_id})")
        return field_id
    except Exception as e:
        print(f"❌ Error al actualizar el campo related: {e}")
        return None

# --- Función para crear permisos ---
def crear_permisos(modelo_id, grupo_id):
    """
    Crea permisos de acceso para un modelo y un grupo específico.
    Si ya existen, los actualiza.
    """
    try:
        # Verificar si el permiso ya existe
        permiso_id = models.execute_kw(
            db, uid, password,
            'ir.model.access', 'search',
            [[['model_id', '=', modelo_id], ['group_id', '=', grupo_id]]]
        )

        if permiso_id:
            # Actualizar el permiso si ya existe
            permiso_id = models.execute_kw(
                db, uid, password,
                'ir.model.access', 'write',
                [permiso_id, {
                    'perm_read': True,
                    'perm_write': True,
                    'perm_create': True,
                    'perm_unlink': True,
                }]
            )
            print(f"✅ Permisos actualizados con éxito (ID: {permiso_id}).")
        else:
            # Crear el permiso si no existe
            permiso_id = models.execute_kw(
                db, uid, password,
                'ir.model.access', 'create',
                [{
                    'name': f'Acceso al modelo {modelo_id} para el grupo {grupo_id}',
                    'model_id': modelo_id,
                    'group_id': grupo_id,
                    'perm_read': True,
                    'perm_write': True,
                    'perm_create': True,
                    'perm_unlink': True,
                }]
            )
            print(f"✅ Permisos creados con éxito (ID: {permiso_id}).")

        return permiso_id
    except Exception as e:
        print(f"❌ Error al crear los permisos: {e}")
        return None

# --- Función para crear vistas ---
def crear_vista(modelo_id, campos, nombre_modelo_descriptivo):
    """
    Crea vistas dinámicas (tree y form) para un modelo basado en sus campos.
    Si ya existen, las actualiza.
    """
    try:
        # Obtener el nombre técnico del modelo
        nombre_modelo_tecnico = models.execute_kw(
            db, uid, password,
            'ir.model', 'read',
            [[modelo_id], ['model']]
        )[0]['model']

        # Crear vista tree
        tree_fields_xml = "\n".join(
            [f'<field name="{c["name"]}" widget="boolean_toggle"/>' if c['ttype'] == 'boolean' else f'<field name="{c["name"]}"/>' for c in campos]
        )
        tree_arch = f"""<?xml version="1.0"?>
        <tree>
            {tree_fields_xml}
        </tree>"""

        # Verificar si la vista tree ya existe
        tree_view_id = models.execute_kw(
            db, uid, password,
            'ir.ui.view', 'search',
            [[['name', '=', f'Vista Árbol de {nombre_modelo_descriptivo}'], ['model', '=', nombre_modelo_tecnico], ['type', '=', 'tree']]]
        )

        if tree_view_id:
            # Actualizar la vista tree si ya existe
            tree_view_id = models.execute_kw(
                db, uid, password,
                'ir.ui.view', 'write',
                [tree_view_id, {'arch': tree_arch}]
            )
            print(f"✅ Vista tree actualizada con éxito (ID: {tree_view_id}).")
        else:
            # Crear la vista tree si no existe
            tree_view_id = models.execute_kw(
                db, uid, password,
                'ir.ui.view', 'create',
                [{
                    'name': f'Vista Árbol de {nombre_modelo_descriptivo}',
                    'model': nombre_modelo_tecnico,
                    'type': 'tree',
                    'arch': tree_arch,
                    'priority': 160,
                }]
            )
            print(f"✅ Vista tree creada con éxito (ID: {tree_view_id}).")

        # Crear vista form
        form_fields_xml = "\n".join(
            [f'<field name="{c["name"]}" widget="boolean_toggle"/>' if c['ttype'] == 'boolean' else f'<field name="{c["name"]}"/>' for c in campos]
        )
        form_arch = f"""<?xml version="1.0"?>
        <form>
            <sheet>
                <group>
                    {form_fields_xml}
                </group>
            </sheet>
        </form>"""

        # Verificar si la vista form ya existe
        form_view_id = models.execute_kw(
            db, uid, password,
            'ir.ui.view', 'search',
            [[['name', '=', f'Vista Formulario de {nombre_modelo_descriptivo}'], ['model', '=', nombre_modelo_tecnico], ['type', '=', 'form']]]
        )

        if form_view_id:
            # Actualizar la vista form si ya existe
            form_view_id = models.execute_kw(
                db, uid, password,
                'ir.ui.view', 'write',
                [form_view_id, {'arch': form_arch}]
            )
            print(f"✅ Vista form actualizada con éxito (ID: {form_view_id}).")
        else:
            # Crear la vista form si no existe
            form_view_id = models.execute_kw(
                db, uid, password,
                'ir.ui.view', 'create',
                [{
                    'name': f'Vista Formulario de {nombre_modelo_descriptivo}',
                    'model': nombre_modelo_tecnico,
                    'type': 'form',
                    'arch': form_arch,
                    'priority': 160,
                }]
            )
            print(f"✅ Vista form creada con éxito (ID: {form_view_id}).")

        return tree_view_id, form_view_id
    except Exception as e:
        print(f"❌ Error al crear las vistas: {e}")
        return None, None

# --- Función para agregar un modelo a un menú (existente o nuevo) ---
def agregar_modelo_a_menu(nombre_modelo, nombre_descriptivo, nombre_menu, nombre_accion, menu_padre_id=None, grupo_id=132):
    """
    Crea un modelo y lo agrega a un menú (existente o nuevo).

    :param nombre_modelo: Nombre técnico del modelo (ej: 'x_nuevo_modelo')
    :param nombre_descriptivo: Nombre descriptivo del modelo (ej: 'Nuevo Modelo')
    :param nombre_menu: Nombre del menú (ej: 'Menú Nuevo Modelo')
    :param nombre_accion: Nombre de la acción (ej: 'Acción Nuevo Modelo')
    :param menu_padre_id: ID del menú padre (opcional, si es None se crea un menú nuevo)
    :param grupo_id: ID del grupo para los permisos (por defecto: 132)
    :return: ID del menú creado o actualizado
    """
    try:
        # Crear el modelo si no existe
        modelo_id = crear_modelo(nombre_modelo, nombre_descriptivo)
        if not modelo_id:
            print(f"❌ No se pudo crear el modelo '{nombre_modelo}'.")
            return None

        # Obtener el nombre técnico del modelo
        nombre_modelo_tecnico = models.execute_kw(
            db, uid, password,
            'ir.model', 'read',
            [[modelo_id], ['model']]
        )[0]['model']

        # Verificar si la acción ya existe
        accion_id = models.execute_kw(
            db, uid, password,
            'ir.actions.act_window', 'search',
            [[['name', '=', nombre_accion], ['res_model', '=', nombre_modelo_tecnico]]]
        )

        if not accion_id:
            # Crear la acción si no existe
            accion_id = models.execute_kw(
                db, uid, password,
                'ir.actions.act_window', 'create',
                [{
                    'name': nombre_accion,
                    'res_model': nombre_modelo_tecnico,
                    'view_mode': 'tree,form',

                }]
            )
            print(f"✅ Acción '{nombre_accion}' creada con éxito (ID: {accion_id}).")
        else:
            accion_id = accion_id[0]
            print(f"⚠️ La acción '{nombre_accion}' ya existe (ID: {accion_id}).")

        # Crear permisos para el modelo
        permisos_id = crear_permisos(modelo_id, grupo_id)

        # Verificar si el menú ya existe
        menu_id = models.execute_kw(
            db, uid, password,
            'ir.ui.menu', 'search',
            [[['name', '=', nombre_menu]]]
        )

        if menu_id:
            # Actualizar el menú existente
            menu_id = models.execute_kw(
                db, uid, password,
                'ir.ui.menu', 'write',
                [menu_id, {'action': f'ir.actions.act_window,{accion_id}'}]
            )
            print(f"✅ Menú '{nombre_menu}' actualizado con éxito (ID: {menu_id}).")
        else:
            # Crear un menú nuevo
            menu_vals = {
                'name': nombre_menu,
                'action': f'ir.actions.act_window,{accion_id}',

            }
            if menu_padre_id:
                menu_vals['parent_id'] = menu_padre_id
            menu_id = models.execute_kw(
                db, uid, password,
                'ir.ui.menu', 'create',
                [menu_vals]
            )
            print(f"✅ Menú '{nombre_menu}' creado con éxito (ID: {menu_id}).")

        return menu_id
    except Exception as e:
        print(f"❌ Error al agregar el modelo al menú: {e}")
        return None

# ----------------------------
# Ejecución
# ----------------------------
if __name__ == "__main__":
    NOMBRE_MODELO = "x_prueba_freddy_2"
    NOMBRE_DESC = "Pruebas Freddy 2"

    menu_id = agregar_modelo_a_menu(
        nombre_modelo=NOMBRE_MODELO,
        nombre_descriptivo=NOMBRE_DESC,
        nombre_menu="Menú Prueba Freddy 2",
        nombre_accion="Acción Prueba Freddy 2",
        menu_padre_id='1624',
        grupo_id=132
    )

    if not menu_id:
        raise SystemExit("No se pudo crear/actualizar el menú. Revisa el error anterior.")

    # Obtener ID de ir.model del modelo técnico
    modelo_id, _ = search_one("ir.model", [["model", "=", NOMBRE_MODELO]], fields=["id"])
    if not modelo_id:
        raise SystemExit("No se encontró el ir.model del modelo recién creado.")

    campos_creados = []

    # 1) Crear many2one x_nombre
    crear_campo(
        modelo_id,
        "x_nombre",
        "many2one",
        "Nombre",
        required=False,
        store=True,
        relation="res.partner"
    )
    campos_creados.append({"name": "x_nombre", "ttype": "many2one"})

    # 2) Crear o actualizar x_name para que tome x_nombre.name
    #    - Si NO existe, se crea como char related.
    #    - Si YA existe, se actualiza con write().
    field_x_name_id, data = search_one(
        "ir.model.fields",
        [["model_id", "=", modelo_id], ["name", "=", "x_name"]],
        fields=["id", "ttype", "related"]
    )

    if not field_x_name_id:
        crear_campo(
            modelo_id,
            "x_name",
            "char",
            "Nombre (Relacionado)",
            related="x_nombre.name",
            store=True,
            readonly=True
        )
        print("✅ Campo x_name creado como related='x_nombre.name'.")
    else:
        actualizar_campo_related(modelo_id, "x_name", "x_nombre.name", store=True, readonly=True)

    campos_creados.append({"name": "x_name", "ttype": "char"})

    # Otros campos de ejemplo
    crear_campo(modelo_id, "x_descripcion", "text", "Descripción")
    campos_creados.append({"name": "x_descripcion", "ttype": "text"})

    crear_campo(modelo_id, "x_fecha", "date", "Fecha")
    campos_creados.append({"name": "x_fecha", "ttype": "date"})

    crear_campo(modelo_id, "x_valor", "float", "Valor")
    campos_creados.append({"name": "x_valor", "ttype": "float"})

    crear_campo(modelo_id, "x_activo", "boolean", "Activo")
    campos_creados.append({"name": "x_activo", "ttype": "boolean"})

    # Crear/actualizar vistas
    vista_tree_id, vista_form_id = crear_vista(modelo_id, campos_creados, NOMBRE_DESC)
    print(f"📌 Vistas listas. Tree ID: {vista_tree_id} | Form ID: {vista_form_id}")