import requests

# json-server storage/zonas.json -b 5009
def getDataZonas():
    peticion = requests.get("http://192.168.1.117:5009")
    data = peticion.json()
    return data


