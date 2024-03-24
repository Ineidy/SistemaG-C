import requests
import re


def getAllDataActivos():
    peticionactivos = requests.get("http://154.38.171.54:5502/activos")
    dataactivos = peticionactivos.json()
    return dataactivos

def postActivos():
    activos = {}
    while True:
        try:
            if not activos.get("NroItem"):
                nmeroitem = int(input("Ingrese el numero de item: "))
                if(re.match(r"^[0-9]+$", nmeroitem)is not None):
                    activos["NroItem"] = nmeroitem
                else:
                    raise Exception ("El numero de item no cumple con los estandares requeridos")
                
            elif not activos.get("CodTransaccion"):
                codigotransaccion = int(input("Ingrese el codigo de la transaccion: "))
                if(re.match(r"^[0-9]+$", codigotransaccion)is not None):
                    activos["CodTransaccion"]=codigotransaccion
                else:
                    raise Exception ("El codigo de transaccion no cumple con los estandares requeridos")
            elif not activos.get("NroSerial"):
                numeroserial = input("Ingrese el numero del serial: ")
                if(re.match(r"^[0-9][A-Z]+$", numeroserial)is not None):
                    activos["CodTransaccion"]=numeroserial
                else:
                    raise Exception ("El numero del serial no cumple con los estandares requeridos")
            elif not activos.get("CodCampus"):
                codigocampus = input("Ingrese el codigo de campus: ")
                if(re.match(r"^[0-9][A-Z]+$", codigocampus)is not None):
                    activos["CodCampus"]=codigocampus
                else:
                    raise Exception ("El codigo de campus no cumple con los estandares requeridos")
            elif not activos.get("NroFormulario"):
                numerofor = int(input("Ingrese el numero de formulario: "))
                if(re.match(r"^[0-9]+$", codigotransaccion)is not None):
                    activos["NroFormulario"]=numerofor
                else:
                    raise Exception ("El numero de formulario no cumple con los estandares requeridos")
            elif not activos.get("Nombre"):
                nombreActivo = input("Ingrese el nombre del activo: ")
                activos["Nombre"]=nombreActivo

                
        except Exception as error:
            print(error)







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
