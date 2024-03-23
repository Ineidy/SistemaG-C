import requests

# json-server storage/categoriaActivos.json -b 5003
def detDataCateActiv():
    peticion = requests.get("http://192.168.1.117:5003")
    data = peticion.json()
    return data