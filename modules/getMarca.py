import requests

# json-server storage/marca.json -b 5005
def getDataMarca():
    peticion = requests.get("http://192.168.1.117:5005")
    data = peticion.json()
    return data