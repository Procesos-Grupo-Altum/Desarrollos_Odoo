# herencia_grupos.py
from Api_conexion import url, db, username, password, uid, models

print("✓ Conectado a Odoo correctamente")
print(f"Usuario ID: {uid}")
print(f"Base de datos: {db}\n")

# ========================================
# CONFIGURACIÓN DE GRUPOS
# ========================================

# Grupos regionales VISE que heredarán otros grupos (IDs numéricos)
grupos_regionales = [
    286,  # Vise Regional Barranquilla
    296,  # Vise Regional Bogota Analistas
    297,  # Vise Regional Bogota Coordinadores
    288,  # Vise Regional Bucaramanga
    285,  # Vise Regional Cali
    292,  # Vise Regional Cartagena
    289,  # Vise Regional Girardot
    287,  # Vise Regional Medellín
    284,  # Vise Regional Pereira
    290,  # Vise Regional Tunja
    291,  # Vise Regional Villavicencio
]

# Grupos base que los regionales deben heredar (IDs numéricos)
grupos_a_heredar = [
    180,  # Vise Contabilidad Anticipos Empleados
    222,  # Vise Contabilidad Gastos Empleados
    279,  # Vise Operaciones Coordinadores
    200,  # Vise Requisiciones
    185,  # Vise Selección
]


# ========================================
# FUNCIONES
# ========================================

def verificar_grupo_existe(group_id):
    """
    Verifica si un grupo existe en la base de datos

    Args:
        group_id (int): ID del grupo

    Returns:
        bool: True si existe, False si no
    """
    try:
        result = models.execute_kw(
            db, uid, password,
            'res.groups', 'search',
            [[['id', '=', group_id]]]
        )
        return len(result) > 0
    except Exception as e:
        print(f"⚠️  Error al verificar grupo {group_id}: {e}")
        return False


def get_group_info(group_id):
    """
    Obtiene información detallada de un grupo

    Args:
        group_id (int): ID del grupo

    Returns:
        dict: Información del grupo
    """
    try:
        group_data = models.execute_kw(
            db, uid, password,
            'res.groups', 'read',
            [[group_id], ['name', 'implied_ids', 'full_name']]
        )
        return group_data[0] if group_data else None
    except Exception as e:
        print(f"❌ Error al obtener info del grupo {group_id}: {e}")
        return None


def agregar_herencia_grupos(grupo_regional_id, grupos_heredar_ids):
    """
    Agrega herencia de grupos a un grupo regional

    Args:
        grupo_regional_id (int): ID del grupo regional
        grupos_heredar_ids (list): Lista de IDs de grupos a heredar

    Returns:
        bool: True si tuvo éxito, False en caso contrario
    """
    # Verificar que el grupo regional existe
    if not verificar_grupo_existe(grupo_regional_id):
        print(f"❌ No se encontró el grupo regional con ID: {grupo_regional_id}\n")
        return False

    # Obtener información actual del grupo
    info_actual = get_group_info(grupo_regional_id)
    if info_actual:
        print(f"📋 Procesando: {info_actual['name']} (ID: {grupo_regional_id})")
        print(f"   Grupos heredados actuales: {info_actual['implied_ids']}")

    # Verificar que los grupos a heredar existen
    ids_validos = []
    for grupo_id in grupos_heredar_ids:
        if verificar_grupo_existe(grupo_id):
            ids_validos.append(grupo_id)
            grupo_info = get_group_info(grupo_id)
            if grupo_info:
                print(f"   ➕ Agregando herencia de: {grupo_info['name']} (ID: {grupo_id})")
        else:
            print(f"   ⚠️  Grupo ID {grupo_id} no encontrado, se omitirá")

    if not ids_validos:
        print(f"⚠️  No se encontraron grupos válidos para heredar\n")
        return False

    # Actualizar el campo implied_ids
    # (4, id) agrega el grupo sin eliminar los existentes
    implied_ids_vals = [(4, gid) for gid in ids_validos]

    try:
        models.execute_kw(
            db, uid, password,
            'res.groups', 'write',
            [[grupo_regional_id], {'implied_ids': implied_ids_vals}]
        )

        # Verificar cambios
        info_nueva = get_group_info(grupo_regional_id)
        if info_nueva:
            print(f"   ✅ Grupos heredados actualizados: {info_nueva['implied_ids']}")

        print(f"✓ Herencia aplicada exitosamente\n")
        return True

    except Exception as e:
        print(f"❌ Error al actualizar grupo {grupo_regional_id}: {e}\n")
        return False


# ========================================
# EJECUCIÓN PRINCIPAL
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("AGREGANDO HERENCIA A GRUPOS REGIONALES")
    print("=" * 60 + "\n")

    exitosos = 0
    fallidos = 0

    for grupo_regional in grupos_regionales:
        resultado = agregar_herencia_grupos(grupo_regional, grupos_a_heredar)
        if resultado:
            exitosos += 1
        else:
            fallidos += 1

    # Resumen
    print("=" * 60)
    print("RESUMEN")
    print("=" * 60)
    print(f"✅ Grupos actualizados exitosamente: {exitosos}")
    print(f"❌ Grupos con errores: {fallidos}")
    print(f"📊 Total procesados: {exitosos + fallidos}")
    print("=" * 60)