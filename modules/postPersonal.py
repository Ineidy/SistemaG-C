
import requests
import re
import json
from tabulate import tabulate







def getDataPersonas():
    peticion = requests.get("http://154.38.171.54:5502/personas")
    data = peticion.json()
    return data

def getpersonasId(id):
    peticion= requests.get(f"http://154.38.171.54:5502/personas/{id}")
    return[peticion.json()] if peticion.ok else []

def postPersonal():
    identificacion = input("ingrese el id: ")
    while True:

        persona = {

    "id": identificacion,
    "nroId (CC, Nit)": input("ingrese el nuevo numero de cedula: "),
    "Nombre": input("Ingrese el nuevo nombre: "),
    "Email": input("ingrese el nuevo correo electronico: "),
    "Telefonos": [
        {
        "movil": {
            "id": identificacion,
            "num": input("Ingrese el nuevo numero de telefono: ")
        },
        "casa": {
            "id": identificacion,
            "num": input("ingrese el nuevo movil de casa: ")
        }
        }]
    }
        

        posicion = requests.post("http://154.38.171.54:5502/personas", data=json.dumps(persona, indent=4))
        res = posicion.json
        tablaactivos = [persona]
        return print(tabulate(tablaactivos, headers="keys", tablefmt='rounded_grid'))

def deletePersonas(id):
    peticion = requests.delete(f"http://154.38.171.54:5502/personas/{id}")
    if peticion.status_code == 200:
        print("Persona Eliminada")

def menuactualizar(id):
    while True:
        print("""
QUE INFORMACION DESEA EDITAR

1. NROID(CC, NIT)
2. NOMBRE
3. EMAIL
4. NUMERO MOVIL
5. NUMERO DE CASA 

""")

        personas ={}
        opcion= int(input("Ingrese la opcion deseada: "))
        if(opcion==1):
            nroId = input("ingrese el nuevo numero de identificacion: ")
            personas["nroId (CC, Nit)"]= nroId
        if(opcion==2):
            name = input("Ingrese el nuevo nombre: ")
            personas["Nombre"] = name
        if(opcion==3):
            email = input("ingrese el nuevo numero de email: ")
            personas["Email"]=email
        if(opcion==4):
            nummovil = input("Ingrese el nuevo numero Movil: ")
            personas["num"] = nummovil
        if(opcion==5):
            numcasa = input("Ingrese el nuevo numero de la casa: ")
            personas["num"] = numcasa


        activoexistente = getDataPersonas()
        if not activoexistente:
            return {"Mensaje": "Activo no encontrado"}
        
        personaactualizado = {**activoexistente[0], **personas}
        peticion = requests.put(f'http://154.38.171.54:5502/personas/{id}', data=json.dumps(personaactualizado))
        res = peticion.json()

        if peticion.status_code == 200:
            res["Mensaje"] =  "Persona actualizada correctamente"
        else: 
            res["Mensaje"] = "Error al actualizar persona"
        return res
    


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
        if(opcion!=1) and (opcion!=2) and (opcion!=3) and (opcion!=4) and (opcion!=5):
            print("Opcion no existente!")
            print("Intenta nuevamente :)")
        elif(opcion==5):
            break
        elif(opcion==1):
            print(tabulate(postPersonal(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==3):
            id = input("Ingresa el id de la persona que quiere elimina: r")
            print(tabulate(deletePersonas(id), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==4): 
            print(menuBusqueda())
        elif(opcion==2):
            id = input("Ingrese el id de la persona que desea actualizar: ")
            print(menuactualizar(id))


def getBuscarPersona(id):
    BuscarPersona= []
    for val in getDataPersonas():
        if(val.get('id')== id):
              BuscarPersona.append({
                "Identificacion": val.get("nroId (CC, Nit)"),
                "nombre": val.get("Nombre"),
                "Email": val.get("Email")
            }
            )
    return BuscarPersona



def getBuscarNroId(cc):
    buscarnrocc= []
    for val in getDataPersonas():
        if(val.get('nroId (CC, Nit)')== cc):
              buscarnrocc.append({
                "Identificacion": val.get("nroId (CC, Nit)"),
                "nombre": val.get("Nombre"),
                "Email": val.get("Email")
            }
            )
    return buscarnrocc


def getBuscarName(name):
    buscarname= []
    for val in getDataPersonas():
        if(val.get('Nombre')== name):
              buscarname.append({
                "Identificacion": val.get("nroId (CC, Nit)"),
                "nombre": val.get("Nombre"),
                "Email": val.get("Email")
            }
            )
    return buscarname

def getBuscarEmail(email):
    buscaremail= []
    for val in getDataPersonas():
        if(val.get('Email')== email):
              buscaremail.append({
                "Identificacion": val.get("nroId (CC, Nit)"),
                "nombre": val.get("Nombre"),
                "Email": val.get("Email")
            }
            )
    return buscaremail


def menuBusqueda():
    while True:
        print("""
              


            MENU DE BUSQUEDA DE PERSONAS

              
            1. BUSCAR PERSONAS POR EL ID
            2. BUSCAR PERSONAS POR EL NROID (CC, NIT)
            3. BUSCAR PERSONA POR EL NOMBRE
            4. BUSCAR PERSONA POR EL EMAIL
            0. SALIR


""")
        opcion = int(input("Ingrese la opcion que desea filtrar: "))
        if(opcion!=1) and (opcion!=2) and (opcion!=3) and (opcion!=4) and (opcion!=0):
            print("Intenta nuevamente :)")
            menuBusqueda()
        elif(opcion==0):
            break
        elif(opcion==1):
            id = input("Ingrese el id de la persona que desea filtrar: ")
            print(tabulate(getBuscarPersona(id), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==2):
            cc = input("Ingrese el NroId que desea filtrar: ")
            print(tabulate(getBuscarNroId(cc), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==3):
            name = input("Ingrese el nombre de la persona que desea filtrar: ")
            print(tabulate(getBuscarName(name), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==4):
            email = input("Ingrese el Email de la persona que desea filtrar: ")
            print(tabulate(getBuscarEmail(email), headers="keys", tablefmt='rounded_grid'))