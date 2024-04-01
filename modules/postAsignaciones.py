import requests
from tabulate import tabulate
import json
import modules.postPersonal as Personal
import modules.postActivos as activos 
from datetime import datetime

class colors:
    RESET = '\033[0m'
    BOLDYELLOW = '\033[1;33m'

def getDataAsignaciones():
    peticionAsignaciones = requests.get("http://154.38.171.54:5502")
    dataAsignaciones = peticionAsignaciones.json()
    return dataAsignaciones

def obtenerAsignaId(id):
    peticionAsigna = requests.get(f"http://154.38.171.54:5502/activos/{id}")
    dataAsignaId= peticionAsigna.json()
    return dataAsignaId

def MenuTipoAsigna():
    while True:
        print(colors.BOLDYELLOW+"""
              
                    QUE TIPO DE ASIGNACION USARA?
                                

                                
                            1. PERSONA
                            2. ZONA
                            0. SALIR

        -SI QUIERE SALIR DE UNA OPCION QUE SELECCIONO, PRESIONE CTROL + C PARA CANCELAR OPCION

"""+colors.RESET)
        try:

            opcion = int(input("Ingrese la opcion deseada: "))
            if opcion not in [1,2,0]:
                print(colors.BOLDYELLOW+"Opcion no existente!"+colors.RESET)
                print(colors.BOLDYELLOW+"Intente nuevamente :)"+colors.RESET)
            if(opcion==0):
                break
            elif(opcion==1):
                postAsignacionesPersona()
            elif(opcion==2):
                postAsignacionesZonas()
        except KeyboardInterrupt:
            return menuAsignacionActivos()



def postAsignacionesPersona(idactivo):

    NroID = input("Ingrese el id de la asignacion: ")
    fechaasig = datetime.now().strftime("%Y-%d-%m"),
    asignadoa = input("Ingrese el id de la zona a la que le asignara el activo: ")
    responsable = input("Ingrese el id del encargado del movimiento del activo: ")

    nuevainfo ={
        "NroAsignacion": NroID,
        "FechaAsignación": fechaasig,
        "TipoAsignacion": "Persona",
        "AsignadoA": asignadoa
    }

    nuevohistorial ={
                "NroId":NroID,
                "FechaAsignacion": fechaasig,
                "TipoMov": "1",
                "idRespMov": responsable
    }

    activo = obtenerAsignaId(idactivo)
    if activo:
        if activo.get("idEstado")== "3":
            print(colors.BOLDYELLOW+"EL ACTIVO ESTA EN RAPARACION Y/O GARANTIA, NO PUEDE SER ASIGNADO"+colors.RESET)
            return False

        if activo.get("idEstado") == "2":
            print(colors.BOLDYELLOW+"EL ACTIVO ESTA DE BAJA, NO PUEDE SER ASIGNADO"+colors.RESET)
            return False
        if activo.get("IdEstado")=="1":
            print(colors.BOLDYELLOW+"EL ACTIVO YA ESTA ASIGNADO"+colors.RESET)
            return False
        if activo.get("idEstado") == "0":
            True

        asignaciones = activo.get("asignaciones", [])
        asignaciones.append(nuevainfo)
        activo["asignaciones"] = asignaciones



        activoH = activo.get("historialActivos", [])
        activoH.append(nuevohistorial)
        activo["historialActivos"] = activoH




        link =  f"http://154.38.171.54:5502/activos/{idactivo}"
        respuesta = requests.put(link, json=activo)
        if respuesta.status_code == 200:
            activo["idEstado"]="1"
            requests.put(link, json=activo)
            print(colors.BOLDYELLOW+"Asignacion guardada correctamente"+colors.RESET)
            return True
        else: 
            print(colors.BOLDYELLOW+"Error al guardad la asignacion"+colors.RESET)
            return False
    else: 
        print(colors.BOLDYELLOW+"Activo no encontrado"+colors.RESET)
        return False
    


def postAsignacionesZonas(idactivo):

    NroID = input("Ingrese el id de la asignacion: ")
    fechaasig = datetime.now().strftime("%Y-%d-%m"),
    asignadoa = input("Ingrese el id de la zona a la que le asignara el activo: ")
    responsable = input("Ingrese el id del encargado del movimiento del activo: ")

    nuevainfo ={
        "NroAsignacion": NroID,
        "FechaAsignación": fechaasig,
        "TipoAsignacion": "Zona",
        "AsignadoA": asignadoa

    }
    nuevohistorial ={
                "NroId":NroID,
                "FechaAsignacion": fechaasig,
                "TipoMov": "1",
                "idRespMov": responsable
    }
    activo = obtenerAsignaId(idactivo)
    if activo:
        if activo.get("idEstado")== "3":
            print(colors.BOLDYELLOW+"EL ACTIVO ESTA EN RAPARACION Y/O GARANTIA, NO PUEDE SER ASIGNADO"+colors.RESET)
            return False
        if activo.get("idEstado") == "0":
            True
        if activo.get("idEstado") == "2":
            print(colors.BOLDYELLOW+"EL ACTIVO ESTA DE BAJA, NO PUEDE SER ASIGNADO"+colors.RESET)
            return False
        if activo.get("IdEstado")=="1":
            print(colors.BOLDYELLOW+"EL ACTIVO YA ESTA ASIGNADO"+colors.RESET)
            return False
        

        asignaciones = activo.get("asignaciones", [])
        asignaciones.append(nuevainfo)
        activo["asignaciones"] = asignaciones

        activoH = activo.get("historialActivos", [])
        activoH.append(nuevohistorial)
        activo["historialActivos"] = activoH




        link =  f"http://154.38.171.54:5502/activos/{idactivo}"
        respuesta = requests.put(link, json=activo)
        if respuesta.status_code == 200:
            activo["idEstado"]="1"


            requests.put(link, json=activo)
            print(colors.BOLDYELLOW+"Asignacion guardada correctamente"+colors.RESET)
            return True
        else: 
            print(colors.BOLDYELLOW+"Error al guardad la asignacion"+colors.RESET)
            return False
    else: 
        print(colors.BOLDYELLOW+"Activo no encontrado"+colors.RESET)
        return False


def menuAsignacionActivos():
    while True:
        print(colors.BOLDYELLOW+"""

              


                            MENU ASIGNACION DE ACTIVOS
                                

                            1. CREAR ASIGNACION
                            2. BUSCAR ASIGNACION
                            3. REGRESAR AL MENU PRINCIPAL


        -SI QUIERE SALIR DE UNA OPCION QUE SELECCIONO, PRESIONE CTROL + C PARA CANCELAR OPCION

"""+colors.RESET)
        try: 
            opcion = int(input("Ingrese una opcion: "))
            if opcion not in [1,2,3]:
                print(colors.BOLDYELLOW+"Opcion no existente!"+colors.RESET)
                print(colors.BOLDYELLOW+"Intente nuevamente :)"+colors.RESET)
            if(opcion==3):
                break
            elif(opcion==1):
                menupersonasOzonas()
            elif(opcion==2):
                id = input("Ingresa el id de del activo del que desea buscar asignaciones")
                print(tabulate(getAllAsignaId(id), headers="keys", tablefmt='rounded_grid'))             
        except KeyboardInterrupt:
            break    


def getAllAsignaId(id):
    asignacionid = []
    for val in activos.getActivosId(id):
        asignaciones = val.get('asignaciones', [])
        for asignacion in asignaciones:
            asignacionid.append({
                    "NroItem": val.get('NroItem'),
                    "NroFormulario": val.get('NroFormulario'),
                    "Nombre": val.get('Nombre'),
                    "idEstado": val.get('idEstado'),
                    "asignaciones =>": val.get(''),
                    "NroAsignacion": asignacion.get('NroAsignacion'),
                    "FechaAsignación":  asignacion.get('FechaAsignación'),
                    "TipoAsignacion": asignacion.get('TipoAsignacion'),
                    "AsignadoA": asignacion.get('AsignadoA')
                    
            })
    return asignacionid


def getAllHistorialId(id):
    historialid =[]
    for val in activos.getActivosId(id):
        historial = val.get('historialActivos', [])
        for historiales in historial:
            historialid.append({
                    "NroItem": val.get('NroItem'),
                    "NroFormulario": val.get('NroFormulario'),
                    "Nombre": val.get('Nombre'),
                    "idEstado": val.get('idEstado'),
                    "historial =>": val.get(''),
                    "NroId": historiales.get('NroId'),
                    "Fecha":  historiales.get('Fecha'),
                    "tipoMov": historiales.get('tipoMov'),
                    "idRespMov": historiales.get('idRespMov')
            })

    return historialid



def menupersonasOzonas(): 
    while True:
        print(colors.BOLDYELLOW+"""
                        QUE TIPO DE ASIGNACION ES:
                                
                                1. PERSONA
                                2. ZONA
                                0. SALIR

        -SI QUIERE SALIR DE UNA OPCION QUE SELECCIONO, PRESIONE CTROL + C PARA CANCELAR OPCION

"""+colors.RESET)
        try: 
            opcion=int(input("Ingrese la opcion que desea: "))
            if opcion not in [1,2,0]:
                print(colors.BOLDYELLOW+"Opcion no existente!"+colors.RESET)
                print(colors.BOLDYELLOW+"Intente nuevamente :)"+colors.RESET)
            if(opcion==1):
                idactivo = input("Ingrese el id del activo al que desea agregarle la asignacion: ")
                postAsignacionesPersona(idactivo)
            elif(opcion==2):
                idactivo = input("Ingrese el id del activo al que desea agregarle la asignacion: ")
                postAsignacionesZonas(idactivo)
            elif(opcion==0):
                break
        except KeyboardInterrupt:
            return menuAsignacionActivos()



# def generar_historial(nro_id, fecha, tipo_movimiento, id_resp_movimiento):
#     historial = {
#         "NroId": nro_id,
#         "Fecha": fecha,
#         "tipoMov": tipo_movimiento,
#         "idRespMov": id_resp_movimiento
#     }
#     return historial
