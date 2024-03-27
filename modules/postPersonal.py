
import requests
import re
from tabulate import tabulate

# json-server storage/personas.json -b 5006
def getDataPersonas():
    peticion = requests.get("http://192.168.1.117:5006")
    data = peticion.json()
    return data


def postPersonal():
    personal={}
    while True:
        try:
            if not personal.get("nroId (CC, Nit)"):
                nroid= input("Ingresa el nroId de la persona: ")
                if(re.match(r'^[0-9]+$', nroid) is not None):
                    personal["nroId (CC, Nit)"] = nroid
                else: 
                    raise Exception ("El NroId no cumple con los estandares establecidos")
            if not personal.get("Nombre"):
                name = input("Ingrese el nombre de la persona: ")
                if(re.match(r'\b[A-Z][a-zA-Z]*\b', name)is not None):
                    personal["Nombre"]= name
                else:
                    raise Exception ("El nombre no cumple los estandares establecidos")
            if not personal.get("Email"):
                email = input("Ingrese el Email de la persona: ")
                if(re.match(r'^[a-z@.]+$', email) is not None):
                    personal["Email"]=email
                else:
                    raise Exception ("El Email no cumple con los estandares establecidos")
            if not personal.get("movil"):
                movil = input("Ingrese el Teléfono de la persona: ")
                if re.match(r'^\+?[0-9\- ]+$', movil):
                    movil = movil
                else:
                    raise Exception("El Teléfono no cumple con los estándares establecidos")




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
