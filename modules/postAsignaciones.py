import requests
import json
import modules.postPersonal as Personal
import modules.postActivos as activos 
from datetime import datetime


def getDataAsignaciones():
    peticionAsignaciones = requests.get("http://154.38.171.54:5502")
    dataAsignaciones = peticionAsignaciones.json()
    return dataAsignaciones

def obtenerAsignaId(idactivo):
    peticionAsigna = requests.get(f"http://154.38.171.54:5502/activos/{idactivo}")
    dataAsignaId= peticionAsigna.json()
    return dataAsignaId

def MenuTipoAsigna():
    while True:
        print("""
              
                    QUE TIPO DE ASIGNACION USARA?
                                

                                
                            1. PERSONA
                            2. ZONA
                            0. SALIR

""")
        opcion = int(input("Ingrese la opcion deseada: "))
        if(opcion==0):
            break
        elif(opcion==1):
            postAsignacionesPersona()


def postAsignacionesPersona(idactivo):
    nuevainfo ={
        "NroAsignacion": +1,
        "FechaAsignación": input("Ingrese la fecha EN EL SIGUIENTE FORMATO:  YYYY-MM-DD: "),
        "TipoAsignacion": "Persona",
        "AsignadoA": input("Ingrese el id de la persona a la que le asignara el activo: ")

    }
    activo = obtenerAsignaId(idactivo)
    if activo:
        asignaciones = activo.get("asignaciones", [])
        asignaciones.append(nuevainfo)
        activo["asignaciones"] = asignaciones

        link =  f"http://154.38.171.54:5502/activos/{idactivo}"
        respuesta = requests.put(link, json=activo)
        if respuesta.status_code == 200:
            print("Asignacion guardada correctamente")
            return True
        else: 
            print("Error al guardad la asignacion")
            return False
    else: 
        print("Activo no encontrado")
        return False
    


def postAsignacionesZonas(idactivo):
    nuevainfo ={
        "NroAsignacion": +1,
        "FechaAsignación": input("Ingrese la fecha EN EL SIGUIENTE FORMATO:  YYYY-MM-DD: "),
        "TipoAsignacion": "Zona",
        "AsignadoA": input("Ingrese el id de la zona a la que le asignara el activo: ")

    }
    activo = obtenerAsignaId(idactivo)
    if activo:
        asignaciones = activo.get("asignaciones", [])
        asignaciones.append(nuevainfo)
        activo["asignaciones"] = asignaciones

        link =  f"http://154.38.171.54:5502/activos/{idactivo}"
        respuesta = requests.put(link, json=activo)
        if respuesta.status_code == 200:
            print("Asignacion guardada correctamente")
            return True
        else: 
            print("Error al guardad la asignacion")
            return False
    else: 
        print("Activo no encontrado")
        return False


def menuAsignacionActivos():
    while True:
        print("""

              


        MENU ASIGNACION DE ACTIVOS
              

        1. CREAR ASIGNACION
        2. BUSCAR ASIGNACION
        3. REGRESAR AL MENU PRINCIPAL

""")
        opcion = int(input("Ingrese una opcion: "))

        if(opcion==3):
            break
        elif(opcion==1):
            menupersonasOzonas()
             




def buscarAsignaciones(Activo, nroasig):
    




def menupersonasOzonas(): 
    while True:
        print("""
                        QUE TIPO DE ASIGNACION ES:
                                
                                1. PERSONA
                                2. ZONA
                                0. SALIR

""")
        opcion=int(input("Ingrese la opcion que desea: "))
        if(opcion==1):
            idactivo = input("Ingrese el id del activo al que desea agregarle la asignacion: ")
            postAsignacionesPersona(idactivo)
        elif(opcion==2):
            idactivo = input("Ingrese el id del activo al que desea agregarle la asignacion: ")
            postAsignacionesZonas(idactivo)
        elif(opcion==0):
             break



# def generar_historial(nro_id, fecha, tipo_movimiento, id_resp_movimiento):
#     historial = {
#         "NroId": nro_id,
#         "Fecha": fecha,
#         "tipoMov": tipo_movimiento,
#         "idRespMov": id_resp_movimiento
#     }
#     return historial
