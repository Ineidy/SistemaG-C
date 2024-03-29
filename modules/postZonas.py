import requests
import json
import re
from tabulate import tabulate


def getDataZonas():
    peticion = requests.get("http://154.38.171.54:5502/zonas")
    data = peticion.json()
    return data


def getPostZonasId(codigo):
    for val in getDataZonas():
        data = list()
        if(val.get("id")== codigo):
            data.append(val)
    return data


def postZonas():
    zonas = {}
    while True: 
        try: 

            if not zonas.get("nombreZona"):
                namezona = input("Ingrese el nombre de la zona: ")
                zonas["nombreZona"] = namezona
            if not zonas.get("totalCapacidad"):

                totcap = input("Ingrese la capacidad total de la zona: ")
                if(re.match(r'[0-9]+$', totcap) is not None):
                    totcap=int(totcap)
                    zonas["totalCapacidad"] = totcap
                else:
                    raise Exception ("La capacidad total no cumple con los estandares establecidos")


        except Exception as error:
            print(error)


        posicion = requests.post("http://154.38.171.54:5502/zonas", data=json.dumps(zonas, indent=4))
        res =posicion.json()
        tablazona = [zonas]
        return print(tabulate(tablazona, headers="keys", tablefmt='rounded_grid'))


def updatezonas(id):
    zonas = {}
    while True:
        try: 
            if not zonas.get("nombreZona"):
                namezona = input("Ingrese el nuevo nombre de la zona: ")
                zonas["nombreZona"] = namezona
            if not zonas.get("totalCapacidad"):
                totcap = input("Ingrese la nueva capacidad total de la zona: ")
                if(re.match(r"^[0-9]+$", totcap)is not None):
                    totcap = int(totcap)
                    zonas["totalCapacidad"] = totcap
                else: 
                    raise Exception ("La nueva capacidad total, no cumple con los estandares")

        except Exception as error:
            print(error)
    
        zonaexistente = getDataZonas()
        if not zonaexistente:
            return {"Mensaje": "Zona no encontrada"}
        
        zonaactualizada = {**zonaexistente[0], **zonas}
        peticion = requests.put(f'http://154.38.171.54:5502/zonas/{id}', data=json.dumps(zonaactualizada))
        res = peticion.json()

        if peticion.status_code == 200:
            res["Mensaje"] = "Zona actualizada correctamente"
        else:
            res["Mensaje"] = "Error al actualizar zona"

        return[res]


def deleteZonas(id):
    peticion = requests.delete(f"http://154.38.171.54:5502/zonas/{id}")
    if peticion.status_code == 200:
        print("Zona Eliminada")


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
        if opcion not in [1,2,3,4,5]:
            print("Opcion no existente!")
            print("Intenta nuevamente :)")
            menuzonas()
        if(opcion==5):
            break
        elif(opcion==1):
            print(tabulate(postZonas(), headers="keys", tablefmt='rounded_grid'))
            print("Zona Guardada Correctamente!")
        elif(opcion==3):
            id = input("Ingrese el id de la zona que desea eliminar: ")
            print(deleteZonas(id))
        elif(opcion==2):
            id = input("Ingrese el id de la zona que desea actualizar: ")
            print(tabulate(updatezonas(id), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==4):
            menubusquedazonas()


def getAllZonasId(id):
    zonasid=[]
    for val in getDataZonas():
        if(val.get('id') == id):
            zonasid.append({
                    "id": val.get('id'),
                    "nombreZona": val.get('nombreZona'),
                    "totalCapacidad": val.get('totalCapacidad')
            })
    return zonasid


def getAllZonasNombre(nombreZona):
    zonasnombre=[]
    for val in getDataZonas():
        if(val.get('nombreZona') == nombreZona):
            zonasnombre.append({
                    "id": val.get('id'),
                    "nombreZona": val.get('nombreZona'),
                    "totalCapacidad": val.get('totalCapacidad')
            })
    return zonasnombre


def getAllZonasCapacidad(totalCapacidad):
    zonascapacidad=[]
    for val in getDataZonas():
        if(val.get('totalCapacidad') == totalCapacidad):
            zonascapacidad.append({
                    "id": val.get('id'),
                    "nombreZona": val.get('nombreZona'),
                    "totalCapacidad": val.get('totalCapacidad')
            })
    return zonascapacidad


def menubusquedazonas():
    while True:
        print("""



        MENU DE BUSQUEDA DE ZONAS
              
        1. BUSCAR POR EL ID
        2. BUSCAR POR EL NOMBRE DE LA ZONA
        3. BUSCAR POR LA CAPACIDAD DE LA ZONA
        4. SALIR AL MENU DE ZONAS
              
""")
        opcion = int(input("Seleccione una opcion: "))
        if opcion not in [1,2,3,4]:
            print("Opcion no existente!")
            print("Intenta nuevamente :)")
            menubusquedazonas()

        if(opcion==1):
            id = input("Ingrese el id de la zona que desea buscar: ")
            print(tabulate(getAllZonasId(id), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==2):
            nombreZona = input("Ingrese el nombre de la zona que desea buscar: ")
            print(tabulate(getAllZonasNombre(nombreZona), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==3):
            totalCapacidad = int(input("Ingresa La capacidad total de la zona que deseas buscar: "))
            print(tabulate(getAllZonasCapacidad(totalCapacidad), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==4):
            break