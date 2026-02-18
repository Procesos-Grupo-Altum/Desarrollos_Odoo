from Api_conexion import odoo_env
import unicodedata

# --- Variables de Conexión ---
url = odoo_env["url"]
db = odoo_env["db"]
uid = odoo_env["uid"]
password = odoo_env["password"]
models = odoo_env["models"]


# --- Helper para generar un nombre base a partir del nombre del grupo ---
def slugify(nombre):
    # Quitar acentos y caracteres raros
    text = unicodedata.normalize('NFKD', nombre).encode('ascii', 'ignore').decode('ascii')
    text = text.lower()
    # Reemplazar espacios y separadores por guion bajo
    result = []
    for ch in text:
        if ch in " -/.":
            result.append("_")
        elif ch.isalnum() or ch == "_":
            result.append(ch)
        # otros caracteres se omiten
    slug = "".join(result)
    # limpiar dobles guiones bajos
    while "__" in slug:
        slug = slug.replace("__", "_")
    return slug.strip("_")


# --- Función para crear un grupo ---
def crear_grupo(nombre, categoria_id=0):
    # Buscar por nombre (igual que ya hacías)
    grupo_ids = models.execute_kw(
        db, uid, password,
        'res.groups', 'search',
        [[('name', '=', nombre)]]
    )
    if grupo_ids:
        grupo_id = grupo_ids[0]
        print(f"ℹ️ El grupo '{nombre}' ya existe. Usando ID: {grupo_id}")
    else:
        grupo_id = models.execute_kw(
            db, uid, password,
            'res.groups', 'create',
            [{
                'name': nombre,
                'category_id': categoria_id,
                'implied_ids': [],
            }]
        )
        print(f"✅ Grupo '{nombre}' creado con ID: {grupo_id}")

    # ---- AQUI CREAMOS EL ID EXTERNO CON EL FORMATO QUE QUIERES ----
    # módulo: "grupo"
    # name: <slug_del_nombre>_<id>
    # Resultado final: grupo.<slug_del_nombre>_<id>
    base_name = slugify(nombre)                     # ej: "vise_tecnologia_promigas_usuario"
    external_name = f"{base_name}_{grupo_id}"       # ej: "vise_tecnologia_promigas_usuario_15"
    module_name = "grupo"                           # => xml_id: grupo.vise_tecnologia_promigas_usuario_15

    # Verificamos si ya existe un ir.model.data para ese grupo, módulo y name
    data_ids = models.execute_kw(
        db, uid, password,
        'ir.model.data', 'search',
        [[
            ('model', '=', 'res.groups'),
            ('module', '=', module_name),
            ('name', '=', external_name),
            ('res_id', '=', grupo_id),
        ]]
    )

    if not data_ids:
        models.execute_kw(
            db, uid, password,
            'ir.model.data', 'create',
            [{
                'name': external_name,
                'model': 'res.groups',
                'module': module_name,
                'res_id': grupo_id,
                'noupdate': True,
            }]
        )
        print(f"🔗 Creado id externo: {module_name}.{external_name} para el grupo ID {grupo_id}")
    else:
        print(f"ℹ️ El id externo {module_name}.{external_name} ya existe para el grupo ID {grupo_id}")

    return grupo_id


def eliminar_grupo(group_id):
    # Verificar si el grupo existe
    grupo_exists = models.execute_kw(
        db, uid, password,
        'res.groups', 'search',
        [[('id', '=', group_id)]]
    )

    if not grupo_exists:
        print(f"❌ No se encontró el grupo con ID: {group_id}")
        return f"No se encontró el grupo con ID: {group_id}"

    # Eliminar el grupo
    models.execute_kw(
        db, uid, password,
        'res.groups', 'unlink',
        [grupo_exists]
    )

    print(f"✅ Grupo eliminado con ID: {group_id}")
    return f"Grupo eliminado exitosamente con ID: {group_id}"


# Lista de grupos a crear (igual que la tuya)
grupos_a_crear = [
    #"Vise Regional Pereira",
    #"Vise Regional Cali",
    #"Vise Regional Barranquilla",
    #"Vise Regional Medellin",
    #"Vise Regional Bucaramanga",
    #"Vise Regional Girardot",
    #"Vise Regional Tunja",
    #"Vise Regional Villavicencio",
    #"Vise Regional Cartagena"
    #"Vise Contrato Airplan",
    #"Vise Contrato Opain",
    #"Vise Regional Bogota Analistas",
    #"Vise Regional Bogota Coordinadores",
    #"Vise Cliente Promigas",
    # "Vise Cliente Surtigas",
    #"Vise Cliente Colsubsidio",
    # 'Vise Servicios Generales',
    # 'Vise Correspondencia',
    # 'Vise Almacen',
    # 'Vise Parque_Automotor_Administrador',
    'Vise Parque_Automotor_Autorizador',
    'Vise Parque_Automotor_Analista',
    # Agrega más grupos según necesites
]

# Crear todos los grupos en la lista
for grupo_nombre in grupos_a_crear:
    grupo_id = crear_grupo(grupo_nombre)
    print(f"Grupo '{grupo_nombre}' creado con ID: {grupo_id}")

# Eliminar un grupo
# eliminar_grupo(group_id=317)

# Lista de IDs de grupos a eliminar
# grupos_a_eliminar = [320]  # Reemplaza con los IDs de los grupos que deseas eliminar

# Eliminar todos los grupos en la lista
# for group_id in grupos_a_eliminar:
#  resultado = eliminar_grupo(group_id)
# print(resultado)
