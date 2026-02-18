import xmlrpc.client


# --- Configuración de conexión Vise Produccion---
# URL = "https://vise.avancyserp.com"
# DB = "vise"
# USERNAME = "analistadatos2@vise.com.co"
# PASSWORD = "e3808fddc59196f9be39970099b1022a8dd36a7c"


# --- Configuración de conexión Base Local---
# URL = "http://localhost:8071"
# DB = "pruebas_dev"
# USERNAME = "pruebas@vise.com.co"
# PASSWORD = "Vise2026*/"


# --- Configuración de conexión Dev-Vise Ambiente de Pruebas---
URL = "https://dev-vise.avancyserp.com"
DB = "dev-vise"
USERNAME = "analistadatos2@vise.com.co"
# PASSWORD = "12345*"
PASSWORD = "e3808fddc59196f9be39970099b1022a8dd36a7c"




# --- Conexión a Odoo ---
common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
uid = common.authenticate(DB, USERNAME, PASSWORD, {})

if not uid:
    raise Exception("❌ Error al conectar a Odoo")

models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object", allow_none=True)

print(f"✅ Conexión exitosa a Odoo {URL} con el usuario {USERNAME}")

# --- Exponer variables para otros archivos ---
odoo_env = {
    "url": URL,
    "db": DB,
    "uid": uid,
    "password": PASSWORD,
    "models": models,
}
