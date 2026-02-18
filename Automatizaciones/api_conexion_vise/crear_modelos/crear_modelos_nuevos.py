from Api_conexion import odoo_env  # Importamos la conexión desde tu archivo

# --- Variables de conexión ---
url = odoo_env["url"]
db = odoo_env["db"]
uid = odoo_env["uid"]
password = odoo_env["password"]
models = odoo_env["models"]

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
                'transient': True,  # Si quieres que
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


# Necesito crear una funcion para crear un menu y agregarle una accion que me permita ver el modelo que cree, pero no se como hacerlo, me puedes ayudar con eso?
def crear_menu(nombre_menu, nombre_accion, modelo_id):
    """
    Crea un menú y una acción para visualizar el modelo creado.
    Si ya existen, los reutiliza.
    """
    try:
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

        # Verificar si el menú ya existe
        menu_id = models.execute_kw(
            db, uid, password,
            'ir.ui.menu', 'search',
            [[['name', '=', nombre_menu], ['action', '=', f'ir.actions.act_window,{accion_id}']]]
        )

        if not menu_id:
            # Crear el menú si no existe
            menu_id = models.execute_kw(
                db, uid, password,
                'ir.ui.menu', 'create',
                [{
                    'name': nombre_menu,
                    'action': f'ir.actions.act_window,{accion_id}',
                }]
            )
            print(f"✅ Menú '{nombre_menu}' creado con éxito (ID: {menu_id}).")
        else:
            menu_id = menu_id[0]
            print(f"⚠️ El menú '{nombre_menu}' ya existe (ID: {menu_id}).")

        return menu_id
    except Exception as e:
        print(f"❌ Error al crear el menú o la acción: {e}")
        return None

        
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
                    'perm_unlink': False,
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


# Necesito crear una funcion para los diferentes tipos de vistas pero que sea dinamica por la cantidad de campos que contenga el modelo, y si los campos con booleanos les coloque el widget (ej: widget='boolean_button') pero no se como hacerlo, me puedes ayudar con eso?
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
                    'priority': 160,  # Valor por defecto para sequence
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
                    'priority': 160,  # Valor por defecto para sequence
                }]
            )
            print(f"✅ Vista form creada con éxito (ID: {form_view_id}).")

        return tree_view_id, form_view_id
    except Exception as e:
        print(f"❌ Error al crear las vistas: {e}")
        return None, None




# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Crear un modelo personalizado
    modelo_id = crear_modelo('x_prueba_freddy', 'Pruebas Freddy')

    # Lista para almacenar los campos creados
    campos_creados = []

    # Crear campos en el modelo
    if modelo_id:
        # Crear campo 'x_nombre' y agregar a la lista de campos
        campo_nombre = crear_campo(modelo_id, 'x_nombre', 'many2one', 'Nombre', required=False, store=True, relation='res.partner')
        if campo_nombre:
            campos_creados.append({'name': 'x_nombre', 'ttype': 'many2one'})

        # Crear campo 'x_descripcion' y agregar a la lista de campos
        campo_descripcion = crear_campo(modelo_id, 'x_descripcion', 'text', 'Descripción')
        if campo_descripcion:
            campos_creados.append({'name': 'x_descripcion', 'ttype': 'text'})

        # Crear campo 'x_fecha' y agregar a la lista de campos
        campo_fecha = crear_campo(modelo_id, 'x_fecha', 'date', 'Fecha')
        if campo_fecha:
            campos_creados.append({'name': 'x_fecha', 'ttype': 'date'})

        # Crear campo 'x_valor' y agregar a la lista de campos
        campo_valor = crear_campo(modelo_id, 'x_valor', 'float', 'Valor')
        if campo_valor:
            campos_creados.append({'name': 'x_valor', 'ttype': 'float'})

        # Crear campo 'x_activo' y agregar a la lista de campos
        campo_activo = crear_campo(modelo_id, 'x_activo', 'boolean', 'Activo')
        if campo_activo:
            campos_creados.append({'name': 'x_activo', 'ttype': 'boolean'})

    # Crear un menú para el modelo
    if modelo_id:
        menu_id = crear_menu('Menú Prueba Freddy', 'Acción Prueba Freddy', modelo_id)

    # Crear permisos para el modelo
    if modelo_id:
        permisos_id = crear_permisos(modelo_id, 132)

    # Crear vistas para el modelo
    if modelo_id and campos_creados:
        vista_tree_id, vista_form_id = crear_vista(modelo_id, campos_creados, 'Pruebas Freddy')
