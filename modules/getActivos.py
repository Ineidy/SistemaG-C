import requests
from tabulate import tabulate


# json-server storage/activos.json -b 5001
def getAllDataActivos():
    peticionactivos = requests.get("http://192.168.1.117:5001")
    dataactivos = peticionactivos.json()
    return dataactivos



def menuActivos():
    while True: 
        print("""
              



        MENU ACTIVOS
              

        1. AGREGAR
        2. EDITAR
        3. ELIMINAR
        4. BUSCAR
        5. REGRESAR AL MENU PRINCIPAL
              

""")
        opcion = int(input("Ingrese una opcion: "))

        if(opcion==5):
            break
