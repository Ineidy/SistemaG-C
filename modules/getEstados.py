import requests

# json-server storage/estados.json -b 5004
def getDataEstados():
    peticiones = requests.get("http://192.168.1.117:5004")
    data = peticiones.json()
    return data