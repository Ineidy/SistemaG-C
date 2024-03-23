import requests

# json-server storage/personas.json -b 5006
def getDataPersonas():
    peticion = requests.get("http://192.168.1.117:5006")
    data = peticion.json()
    return data


def menuPersonal():
    while True:
        print("""
              



        MENU PERSONAL 
              

        1. AGREGAR
        2. EDITAR
        3. ELIMINAR
        4. BUSCAR
        5. REGRESAR AL MENU PRINCIPAL
              

""")
        opcion = int(input("Ingrese una opcion: "))

        if(opcion==5):
            break
