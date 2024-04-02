import requests
from tabulate import tabulate
import json
import modules.postPersonal as Personal
import modules.postZonas as Zonas
import modules.postActivos as activos 
from datetime import datetime
import re

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
        try: 
            print(colors.BOLDYELLOW+"""
              
                    QUE TIPO DE ASIGNACION USARA?
                                

                                
                            1. PERSONA
                            2. ZONA
                            0. SALIR

        -SI QUIERE SALIR DE UNA OPCION QUE SELECCIONO, PRESIONE CTROL + C PARA CANCELAR OPCION

"""+colors.RESET)
        

            opcion = input("Ingrese una opcion: ")
            if re.match(r'^[0-2]$', opcion) is not None:
                opcion = int(opcion)
            if(opcion==0):
                break
            elif(opcion==1):
                postAsignacionesPersona()
            elif(opcion==2):
                postAsignacionesZonas()
        except KeyboardInterrupt:
            return menuAsignacionActivos()



def postAsignacionesPersona(idactivo):
    try: 
        asignadoa = input("Ingrese el id de la Persona a la que le asignara el activo: ")
        responsable = input("Ingrese el id del encargado del movimiento del activo: ")

        responsable_existente = None
        for person in Personal.getDataPersonas():
            if person.get("id") == responsable or person.get("id") == int(responsable):
                responsable_existente = person
                break
        if not responsable_existente:
            print("No Existe Una Persona Con Este Id :C ")
            return

        persona_existente = None
        for person in Personal.getDataPersonas():
            if person.get("id") == asignadoa or person.get("id") == int(asignadoa):
                persona_existente = person
                break
        if not persona_existente:
            print("No Existe Una Persona Con Este Id :C ")
            return

        activo_encontrado = None
        for val in activos.getAllDataActivos():
            if val.get("id") == idactivo or val.get("id") == int(idactivo):
                activo_encontrado = val
                break
        if not activo_encontrado:
            print("No existe un activo con este id :C ")
            return

        nuevainfo ={
            "NroAsignacion": (idactivo),
            "FechaAsignacion": datetime.now().strftime("%Y-%d-%m"),
            "TipoAsignacion": "Persona",
            "AsignadoA": asignadoa
        }

        nuevohistorial ={
                    "NroId":(idactivo),
                    "FechaAsignacion": datetime.now().strftime("%Y-%d-%m"),
                    "TipoMov": "1",
                    "idRespMov": responsable
        }

        activo = obtenerAsignaId(idactivo)
        if activo:
            if activo.get("idEstado")== "3":
                print(colors.BOLDYELLOW+"EL ACTIVO ESTA EN RAPARACION Y/O GARANTIA, NO PUEDE SER ASIGNADO"+colors.RESET)
                return False
            if activo.get("idEstado")=="1":
                print(colors.BOLDYELLOW+"EL ACTIVO YA ESTA ASIGNADO"+colors.RESET)
                return False

            if activo.get("idEstado") == "2":
                print(colors.BOLDYELLOW+"EL ACTIVO ESTA DE BAJA, NO PUEDE SER ASIGNADO"+colors.RESET)
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
        
    except KeyboardInterrupt:
        return


def postAsignacionesZonas(idactivo):
    try: 
        asignadoa = input("Ingrese el id de la zona a la que le asignara el activo: ")
        responsable = input("Ingrese el id del encargado del movimiento del activo: ")


        responsable_existente = None
        for person in Zonas.getDataZonas():
            if person.get("id") == responsable or person.get("id") == int(responsable):
                responsable_existente = person
                break
        if not responsable_existente:
            print("No Existe Una Zona Con Este Id :C ")
            return

        persona_existente = None
        for person in Personal.getDataPersonas():
            if person.get("id") == asignadoa or person.get("id") == int(asignadoa):
                persona_existente = person
                break
        if not persona_existente:
            print("No Existe Una Persona Con Este Id :C ")
            return

        activo_encontrado = None
        for val in activos.getAllDataActivos():
            if val.get("id") == idactivo or val.get("id") == int(idactivo):
                activo_encontrado = val
                break
        if not activo_encontrado:
            print("No existe un activo con este id :C ")
            return

        nuevainfo ={
            "NroAsignacion":(idactivo), 
            "FechaAsignacion": datetime.now().strftime("%Y-%d-%m"),
            "TipoAsignacion": "Zona",
            "AsignadoA": asignadoa

        }
        nuevohistorial ={
                    "NroId":(idactivo), 
                    "FechaAsignacion": datetime.now().strftime("%Y-%d-%m"),
                    "TipoMov": "1",
                    "idRespMov": responsable
        }
        activo = obtenerAsignaId(idactivo)
        if activo:
            if activo.get("idEstado")== "3":
                print(colors.BOLDYELLOW+"EL ACTIVO ESTA EN RAPARACION Y/O GARANTIA, NO PUEDE SER ASIGNADO"+colors.RESET)
                return False
            
            if activo.get("idEstado")=="1":
                print(colors.BOLDYELLOW+"EL ACTIVO YA ESTA ASIGNADO"+colors.RESET)
                return False
            
            if activo.get("idEstado") == "0":
                True
            if activo.get("idEstado") == "2":
                print(colors.BOLDYELLOW+"EL ACTIVO ESTA DE BAJA, NO PUEDE SER ASIGNADO"+colors.RESET)
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
        
    except KeyboardInterrupt:
        return

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
            opcion = input("Ingrese una opcion: ")
            if re.match(r'^[1-5]$', opcion) is not None:
                opcion = int(opcion)

            if(opcion==3):
                break
            elif(opcion==1):
                menupersonasOzonas()
            elif(opcion==2):
                id = input("Ingresa el id de del activo del que desea buscar asignaciones")
                print(tabulate(getAllAsignaId(id), headers="keys", tablefmt='rounded_grid'))             
        except KeyboardInterrupt:
            break    


def getAllAsignaId():


    asignacionid = []
    for val in activos.getAllDataActivos():
        asignaciones = val.get("asignaciones", [])
        for asignacion in asignaciones:
            asignacionid.append({
                    "NroItem": val.get('NroItem'),
                    "NroFormulario": val.get('NroFormulario'),
                    "Nombre": val.get('Nombre'),
                    "idEstado": val.get('idEstado'),
                    "asignaciones =>":val.get(""),
                    "NroAsignacion": asignacion.get("NroAsignacion"),
                    "FechaAsignacion":  asignacion.get('FechaAsignacion'),
                    "TipoAsignacion": asignacion.get('TipoAsignacion'),
                    "AsignadoA": asignacion.get('AsignadoA')
                    
            })
    return asignacionid


def getAllHistorialId(id):

    historialid =[]
    activo_encontrado = None
    for val in activos.getAllDataActivos():
        if val.get("id") == id:
            activo_encontrado = val
            break
    if not activo_encontrado:
        print("No existe un activo con este id :C ")
        return

    historial = val.get('historialActivos', [])
    for historiales in historial:
        historialid.append({
                "NroItem": val.get('NroItem'),
                "NroFormulario": val.get('NroFormulario'),
                "Nombre": val.get('Nombre'),
                "idEstado": val.get('idEstado'),
                "historial => ": val.get(''),
                "tipoMov": historiales.get('TipoMov'),
                "FechaAsignacion":  historiales.get('FechaAsignacion'),
                "TipoMov": historiales.get('TipoMov'),
                "idRespMov": historiales.get('idRespMov')
        })

    return historialid



def menupersonasOzonas(): 
    while True:
        print(colors.BOLDYELLOW+"""
                        QUE TIPO DE ASIGNACION ES:
                                
                                1. PERSONA
                                2. ZONA

        -SI QUIERE SALIR DE UNA OPCION QUE SELECCIONO, PRESIONE CTROL + C PARA CANCELAR OPCION

"""+colors.RESET)
        try: 
            opcion = input("Ingrese una opcion: ")
            if re.match(r'^[1-5]$', opcion) is not None:
                opcion = int(opcion)

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


