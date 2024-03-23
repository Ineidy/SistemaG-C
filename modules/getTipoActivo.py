import requests

# json-server storage/tipoActivo.json -b 5008
def getDataTipoActivos():
    peticion = requests.get("http://192.168.1.117:5008")
    data = peticion.json()
    return data