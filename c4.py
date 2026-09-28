network_config_2 = {
    "0001": {
        "ip" : "192.168.0.2",
        "device": "Switch",
        "policy": "Deny All",
        "status": False,
        "lista": [1, 4, 6, 0, 8]
    },
    "0002": {
        "ip" : "192.168.0.1",
        "device": "Firewall",
        "policy": "Avoid .2 .3 .4",
        "status": True
    },
    "0003": {
        "ip" : "192.168.0.3",
        "device": "Router",
        "policy": "Avoid .2 .4",
        "status": True
    },
    "0004": {
        "ip" : "192.168.0.4",
        "device": "Switch2",
        "policy": "Allow All",
        "status": True
    },
    "0005": {
        "ip" : "192.168.0.5",
        "device": "Access Point",
        "policy": "Allow All",
        "status": True
    }
}
contenido = network_config_2.get("0001")
listaA = contenido.get("lista")
num = listaA[2]
#print(network_config_2.get("0001").get("lista")[2])
print(num)