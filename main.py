# ==== Catálogo de especies con múltiples atributos ====
especies = [
    {"nombre": "Pato criollo", "habitat": "laguna", "vuelo": "corto"},
    {"nombre": "Pato picazo", "habitat": "río", "vuelo": "largo"},
    {"nombre": "Pato colorado", "habitat": "laguna", "vuelo": "corto"},
    {"nombre": "Pato cutirí", "habitat": "humedal", "vuelo": "medio"},
    {"nombre": "Pato barcino", "habitat": "río", "vuelo": "medio"},
    {"nombre": "Pato cuchara", "habitat": "laguna", "vuelo": "medio"},
    {"nombre": "Pato maicero", "habitat": "humedal", "vuelo": "largo"},
    {"nombre": "Pato overo", "habitat": "río", "vuelo": "largo"}
]

# ==== Base de usuarios ====
usuarios = {
    "pato@correo.com": "1234",
    "admin@correo.com": "admin"
}

# ==== Datos de comportamiento para visualización ====
comportamiento_por_especie = {
    "pato picazo": [("vuelo", 3), ("nado", 5), ("sonido", 2)],
    "pato criollo": [("nado", 4), ("vuelo", 2), ("sonido", 3)]
}

# ==== DU09 – Ver ficha completa de especie ====
def obtener_ficha_especie(nombre):
    for especie in especies:
        if especie["nombre"].lower() == nombre.lower():
            return especie
    return None

# ==== DU11 – Filtrar especies por tipo de vuelo ====
def filtrar_por_tipo_de_vuelo(tipo):
    return [e["nombre"] for e in especies if e["vuelo"].lower() == tipo.lower()]

# ==== DU16 – Autenticación por correo y contraseña ====
def autenticar_usuario(email, password):
    return usuarios.get(email) == password

# ==== DU27 – Visualizar comportamiento en gráfico ====
def obtener_datos_comportamiento(nombre):
    return comportamiento_por_especie.get(nombre.lower(), [])

# ==== DU35 – Comparar especies ====
def comparar_especies(nombre1, nombre2):
    e1 = next((e for e in especies if e["nombre"].lower() == nombre1.lower()), None)
    e2 = next((e for e in especies if e["nombre"].lower() == nombre2.lower()), None)
    return (e1, e2)

# ==== DU14 – Buscar especie por nombre ====
def buscar_especie_por_nombre(nombre):
    return [e["nombre"] for e in especies if nombre.lower() in e["nombre"].lower()]

# ==== DU15 – Filtrar especies por hábitat ====
def filtrar_especies_por_habitat(habitat):
    return [e["nombre"] for e in especies if e["habitat"].lower() == habitat.lower()]

# ==== DU08 – Simular comportamiento por hábitat ====
def simular_comportamiento(temperatura, estacion, usuario_tipo):
    if usuario_tipo != "premium":
        return "Funcionalidad exclusiva para usuarios premium"
    if temperatura == "fría":
        return "El pato está nadando para entrar en calor."
    elif temperatura == "templada":
        return "El pato emite su sonido característico."
    elif temperatura == "caliente":
        if estacion == "verano":
            return "El pato vuela alto en verano."
        else:
            return "El pato vuela bajo."
    return "Condiciones desconocidas"
