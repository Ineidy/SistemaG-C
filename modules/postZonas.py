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
            numeroid = str(int(zonas[-1]["id"])+1) if zonas else '1'
            print ("Nuevo Id de la zona: ", numeroid)

            
            if not zonas.get("nombreZona"):
                namezona = input("Ingrese el nombre de la zona: ")
                zonas["nombreZona"] = namezona
            if not zonas.get("totalCapacidad"):
                totcap = int(input("Ingrese la capacidad total de la zona (SOLO NUMEROS): "))
                zonas["totalCapacidad"] = totcap
             


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





def getAllZonasId(id):
    peticion = requests.get(f"http:// 154.38.171.54:5502/zonas/{id}")
    return[peticion.json()] if peticion.ok else []

def getAllZonasNombre(nombreZona):
    peticionnom = requests.get(f"http://154.38.171.54:5502/zonas/{nombreZona}")
    return[peticionnom.json()] if peticionnom.ok else []

def getAllZonasCapacidad(totalCapacidad):
    peticioncap = requests.get(f"http://154.38.171.54:5502/zonas/{totalCapacidad}")
    return[peticioncap.json()] if peticioncap.ok else []





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
        if(opcion!=1) and (opcion!=2) and (opcion!=3) and (opcion!=4) and (opcion!=5):
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
        if(opcion!=1) and (opcion!=2) and (opcion!=3) and (opcion!=4):
            print("Opcion no existente!")
            print("Intenta nuevamente :)")
            menubusquedazonas()

        if(opcion==1):
            id = input("Ingrese el id de la zona que desea buscar: ")
            print(tabulate(getAllZonasId(id), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==2):
            nombrezona = input("Ingrese el nombre de la zona que desea buscar: ")
            print(tabulate(getAllZonasNombre(nombrezona), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==3):
            totalCapacidad = input("Ingresa La capacidad total de la zona que deseas buscar: ")
            print(tabulate(getAllZonasCapacidad(totalCapacidad), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==4):
            break