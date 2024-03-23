import requests
import json
import tabulate


def postZonas():
    zonas = {
        "id" : int(input("Ingrese el Id de la zona: ")),
        "nombreZona": input("Ingrese el nombre de la zona: "),
        "totalCapacidad": int(input("Ingrese la capacidad total de la zona: "))
    }

    posicion = requests.post("http://192.168.1.117:5009", data=json.dumps(zonas))
    res =posicion.json()
    res["Mensaje"] = "Zona Guardada"
    return res



def menuzonas():
    while True:
        print("""



              
        MENU ZONAS
              

        1. AGREGAR
        2. EDITAR
        3. ELIMINAR
        4. BUSCAR
        5. REGRESAR AL MENU PRINCIPAL

""")
        opcion = int(input("Ingrese una opcion: ")) 

        if(opcion==5):
            break
        elif(opcion==1):
            print(tabulate(postZonas(), headers="Keys", tablefmt='rounded_grid'))