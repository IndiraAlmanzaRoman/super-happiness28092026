from flask import Flask, jsonify
import json

with open("API.json", "r", encoding="uft-8") as json_api:
    datos_json = json.load(json_api)
print (datos_json)

app = Flask(__name__)  # espacio dentro de memoria

# Diccionario global para que todas las rutas puedan acceder y modificarlo
dispositivos = {
    101: {
        "ip": "192.168.1.10",
        "device_name": "Router Principal",
        "policy": {"type": "ALLOW_ALL"},
        "status": "Activo"
    },
    102: {
        "ip": "192.168.1.20",
        "device_name": "Switch Piso 1",
        "policy": {"type": "BLOCK_IP", "blocked_ip": "192.168.1.20"},
        "status": "Activo"
    },
    103: {
        "ip": "192.168.1.30",
        "device_name": "Firewall",
        "policy": {"type": "RESTRICT"},
        "status": "Inactivo"
    },
    104: {
            "ip": "192.168.1.40",
            "device_name": "Servidor Web",
            "policy": {
            "type": "REQUIRED_IP",
            "required_ip": "192.168.1.50"
                    },
            "status": "Inactivo"
        },
    105: {
            "ip": "192.168.1.50",
            "device_name": "Access Point",
            "policy": {
    
            "type": "ALLOW_ALL"
            },
            "status": "Activo"
            },
                
    # Elementos nuevos
    106: {
        "ip": "192.168.1.60",
        "device_name": "Servidor Web",
        "policy": {"type": "ALLOW_ALL"},
        "status": "Activo"
    },
    107: {
        "ip": "192.168.1.70",
        "device_name": "Base de Datos",
        "policy": {"type": "INTERNAL_ONLY"},
        "status": "Activo"
    },
    108: {
        "ip": "192.168.1.80",
        "device_name": "Access Point Recepción",
        "policy": {"type": "GUEST_WIFI"},
        "status": "Inactivo"
    },
    109: {
        "ip": "192.168.1.90",
        "device_name": "Switch Piso 2",
        "policy": {"type": "ALLOW_ALL"},
        "status": "Activo"
    },
    110: {
        "ip": "192.168.1.100",
        "device_name": "Cámara de Seguridad",
        "policy": {"type": "VIDEO_ONLY"},
        "status": "Activo"
    }
}

# Lista global para la función de agregar elementos
registro_nombres = ["Router Principal"]

# Endpoint HTML original
@app.route('/')
def inicio():
    print("Cambio")
    return datos_json

# Endpoint JSON original modificado para devolver el diccionario global
@app.route('/api/saludo')
def saludo():
    return jsonify(dispositivos)


@app.route('/api/dispositivo/<int:id_disp>')
def obtener_dispositivo(id_disp):
    """
    Autor: Indira Almanza Roman
    Fecha: 23092026
    Funcion que retorna un elemento segun su ID
    
    """
    if id_disp in dispositivos:
        return jsonify(dispositivos[id_disp])
    return jsonify({"error": "Dispositivo no encontrado"}), 404


@app.route('/api/activos')
def obtener_activos():
    """
    
    """
    activos = {}
    for key, value in dispositivos.items():
        if value["status"] == "Activo":
            activos[key] = value
    return jsonify(activos)

# 3. Mostrar solo los dispositivos Inactivos usando un ciclo for
@app.route('/api/inactivos')
def obtener_inactivos():
    inactivos = {}
    for key, value in dispositivos.items():
        if value["status"] == "Inactivo":
            inactivos[key] = value
    return jsonify(inactivos)

# 4. Obtener solo los nombres de todos los dispositivos
@app.route('/api/nombres')
def obtener_nombres():
    nombres = []
    for value in dispositivos.values():
        nombres.append(value["device_name"])
    return jsonify({"nombres_dispositivos": nombres})

# 5. Buscar un dispositivo por su IP exacta
@app.route('/api/buscar_ip/<ip_buscada>')
def buscar_por_ip(ip_buscada):
    for key, value in dispositivos.items():
        if value["ip"] == ip_buscada:
            return jsonify({key: value})
    return jsonify({"mensaje": "IP no encontrada"})

# 6. Cambiar el estado de un dispositivo específico
@app.route('/api/cambiar_estado/<int:id_disp>/<nuevo_estado>')
def cambiar_estado(id_disp, nuevo_estado):
    if id_disp in dispositivos:
        dispositivos[id_disp]["status"] = nuevo_estado
        return jsonify({"mensaje": "Estado actualizado", "dispositivo": dispositivos[id_disp]})
    return jsonify({"error": "Dispositivo no encontrado"})

# 7. Cambiar TODOS los dispositivos a "Inactivo" usando un ciclo
@app.route('/api/apagar_todos')
def apagar_todos():
    for key in dispositivos:
        dispositivos[key]["status"] = "Inactivo"
    return jsonify({"mensaje": "Todos los dispositivos han sido apagados", "datos": dispositivos})

# 8. Cambiar TODOS los dispositivos a "Activo" usando un ciclo
@app.route('/api/encender_todos')
def encender_todos():
    for key in dispositivos:
        dispositivos[key]["status"] = "Activo"
    return jsonify({"mensaje": "Todos los dispositivos han sido encendidos", "datos": dispositivos})

# 9. Obtener una lista de todos los tipos de políticas de seguridad
@app.route('/api/politicas')
def obtener_politicas():
    politicas = []
    for value in dispositivos.values():
        tipo = value["policy"]["type"]
        if tipo not in politicas: # Evitar duplicados
            politicas.append(tipo)
    return jsonify({"tipos_de_politicas": politicas})

# 10. Actualizar la IP de un dispositivo específico
@app.route('/api/cambiar_ip/<int:id_disp>/<nueva_ip>')
def cambiar_ip(id_disp, nueva_ip):
    if id_disp in dispositivos:
        dispositivos[id_disp]["ip"] = nueva_ip
        return jsonify({"mensaje": "IP actualizada exitosamente", "dispositivo": dispositivos[id_disp]})
    return jsonify({"error": "Dispositivo no encontrado"})


# --- 1 FUNCIÓN PARA AGREGAR A UNA LISTA ---

# Agregar un nuevo nombre a la lista global 'registro_nombres'
@app.route('/api/lista/agregar/<nuevo_nombre>')
def agregar_a_lista(nuevo_nombre):
    registro_nombres.append(nuevo_nombre)
    return jsonify({
        "mensaje": "Elemento agregado a la lista", 
        "lista_actualizada": registro_nombres
    })

if __name__ == '__main__':
    app.run(debug=True)