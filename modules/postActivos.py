import requests
import re
import json
from tabulate import tabulate
from datetime import datetime
import modules.movimientosActivos as mov
import main as main
import modules.postPersonal as Personal

class colors:
    RESET = '\033[0m'
    BOLDYELLOW = '\033[1;33m'



def obtenerAsignaId(id):
    peticionAsigna = requests.get(f"http://154.38.171.54:5502/activos/{id}")
    dataAsignaId= peticionAsigna.json()
    return dataAsignaId

def getAllDataActivos():
    peticionactivos = requests.get("http://154.38.171.54:5502/activos")
    dataactivos = peticionactivos.json()
    return dataactivos

def getActivosId(id):
    peticion= requests.get(f"http://154.38.171.54:5502/activos/{id}")
    return[peticion.json()] if peticion.ok else []



def getAllActivosId(id):
    idactivos=[]
    for val in getAllDataActivos():
        if(val.get('totalCapacidad') == id):
            idactivos.append({
                    "id": val.get('id'),
                    "NroItem": val.get('NroItem'),
                    "Nombre": val.get('Nombre'),
                    "ValorUnitario": val.get('ValorUnitario')
            })
    return idactivos

def deleteactivos(id):
    try: 

        activo_encontrado = None
        for val in getAllDataActivos():
            if val.get("id") == id:
                activo_encontrado = val
                break
        if not activo_encontrado:
            print("No existe un activo con este id :C ")
            return

        respMov= input("Ingrese el id de el responsable de el movimiento: ")
        persona_existente = None
        for person in Personal.getDataPersonas():
            if person.get("id") == respMov or person.get("id") == int(respMov):
                persona_existente = person
                break
        if not persona_existente:
            print("No Existe Una Persona Con Este Id :C ")
            return menuActivos()

        historial={
            "NroId": (id),
            "Fecha":datetime.now().strftime("%Y-%d-%m"),
            "tipoMov": "2",
            "idRespMov": respMov
        }
        activo_encontrado["historialActivos"].append(historial)

        Activoactualizado = {**activo_encontrado, "idEstado": "2"}
        peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(Activoactualizado))
        res = peticion.json()

        if peticion.status_code == 200:
            res["Mensaje"] = "Estado actualizado correctamente!"

        else: 
            res["Mensaje"] = "Error en la actualizacion del estado!"
        return [res]
     
    except KeyboardInterrupt:
        return menuActivos()
    

def cambiarEstadoa0(id):
    activo = getActivosId(id)
    



    if not activo:
        return{"mensaje": "Activo no encontrado"}
    if activo.get["idEstado"] == "2":
        print("ACTIVO DADO DE BAJA, NO SE PUEDE RETORNAR ")
        False

    activo = activo[0]

    historial={
        "NroId": (id),
        "Fecha":datetime.now().strftime("%Y-%d-%m"),
        "tipoMov": "2",
        "idRespMov": input("Ingrese el id de el responsable de el movimiento: ")
    }
    activo["historialActivos"].append(historial)


    Activoactualizado = {**activo, "idEstado": "0"}
    peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(Activoactualizado))
    res = peticion.json()

    if peticion.status_code == 200:
        res["Mensaje"] = "Activo retornado correctamente!"

    else: 
        res["Mensaje"] = "Error en la retornar el activo!"
    return [res]



def cambiarEstadoa2(id):
    activo = getActivosId(id)
    if not activo:
        return{"mensaje": "Activo no encontrado"}
    
    activo = activo[0]

    historial={
        "NroId": (id),
        "Fecha":datetime.now().strftime("%Y-%d-%m"),
        "tipoMov": "2",
        "idRespMov": input("Ingrese el id de el responsable de el movimiento: ")
    }
    activo["historialActivos"].append(historial)


    Activoactualizado = {**activo, "idEstado": "2"}
    peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(Activoactualizado))
    res = peticion.json()

    if peticion.status_code == 200:
        res["Mensaje"] = "Activo retornado correctamente!"

    else: 
        res["Mensaje"] = "Error en la retornar el activo!"
    return [res]



def reasignar(id):

    NroID = input("Ingrese el id de la asignacion: ")

    fechaasig = datetime.now().strftime("%Y-%d-%m"),
    personaozona = input("Ingrese el TipoAsignacion (Persona) o (Zona): "),
    asignadoa = input("Ingrese el id de la Persona o Zona a la que le ReAsignara el activo: ")
    responsable = input("Ingrese el id del encargado del ReAsignamiento del activo: ")

    nuevainfo ={
        "NroAsignacion": NroID,
        "FechaAsignación": fechaasig,
        "TipoAsignacion": personaozona,
        "AsignadoA": asignadoa
    }

    nuevohistorial ={
                "NroId":NroID,
                "FechaAsignacion": fechaasig,
                "TipoMov": "4",
                "idRespMov": responsable
    }

    activo = obtenerAsignaId(id)
    if activo:
        if activo.get("idEstado")== "3":
            print(colors.BOLDYELLOW+"EL ACTIVO ESTA EN RAPARACION Y/O GARANTIA, NO PUEDE SER ASIGNADO"+colors.RESET)
            return 

        if activo.get("idEstado") == "2":
            print(colors.BOLDYELLOW+"EL ACTIVO ESTA DE BAJA, NO PUEDE SER ASIGNADO"+colors.RESET)
            return 
        

        if activo.get("idEstado") == "1":
            True

        asignaciones = activo.get("asignaciones", [])
        asignaciones.append(nuevainfo)
        activo["asignaciones"] = asignaciones



        activoH = activo.get("historialActivos", [])
        activoH.append(nuevohistorial)
        activo["historialActivos"] = activoH




        link =  f"http://154.38.171.54:5502/activos/{id}"
        respuesta = requests.put(link, json=activo)
        if respuesta.status_code == 200:
            activo["idEstado"]="1"
            True
            requests.put(link, json=activo)
            print(colors.BOLDYELLOW+"Activo ReAsignado correctamente"+colors.RESET)
            return 
        else: 
            print(colors.BOLDYELLOW+"Error al ReAsignar el Activo"+colors.RESET)
            return 
    else: 
        print(colors.BOLDYELLOW+"Activo no encontrado"+colors.RESET)
        return 
    




def cambiarEstadoa3(id):

        activo = getActivosId(id)
        if not activo:
            return{"mensaje": "Activo no encontrado"}
        
        activo = activo[0]

        historial={
            "NroId": (id),
            "Fecha":datetime.now().strftime("%Y-%d-%m"),
            "tipoMov": "3",
            "idRespMov": input("Ingrese el id de el responsable de el movimiento: ")
        }
        activo["historialActivos"].append(historial)


        Activoactualizado = {**activo, "idEstado": "3"}
        peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(Activoactualizado))
        res = peticion.json()

        if peticion.status_code == 200:
            res["Mensaje"] = "Activo retornado correctamente!"

        else: 
            res["Mensaje"] = "Error en la retornar el activo!"
        return [res]



def postActivos():

        activos = {}
        try:

            if not activos.get("NroItem"):
                nmeroitem = input("Ingrese el numero de item (SOLO NUMEROS): ")
                if(re.match(r"[0-9]+$", nmeroitem)):
                    nmeroitem = int(nmeroitem)
                    activos["NroItem"] = nmeroitem
                else: 
                    raise Exception("El NroItem no cumple con los requisitos establecidos ")
            if not activos.get("CodTransaccion"):
                activos["CodTransaccion"]=int(327)

            if not activos.get("NroSerial"):
                numeroserial = input("Ingrese el numero del serial(5-10 CARACTERES ENTRE LETRAS MAYUSCULAS Y NUMEROS): ")
                if(re.match(r"^[A-Z0-9]{5,10}$", numeroserial)is not None):
                    activos["NroSerial"]=numeroserial
                else:
                    raise Exception ("El numero del serial no cumple con los estandares requeridos")
            if not activos.get("CodCampus"):
                codigocampus = input("Ingrese el codigo de campus(5-10 CARACTERES ENTRE LETRAS MAYUSCULAS Y NUMEROS): ")
                if(re.match(r"^[A-Z0-9-]{5,10}$", numeroserial)is not None):
                    activos["CodCampus"]=codigocampus
                else:
                    raise Exception ("El codigo de campus no cumple con los estandares requeridos")
            if not activos.get("NroFormulario"):
                numerofor = input("Ingrese el numero de formulario(SOLO NUMEROS): ")
                if(re.match(r'[0-9]+$', numerofor) is not None):
                    numerofor= int(numerofor)
                activos["NroFormulario"]=numerofor
                # else:
                #     raise Exception ("El numero de formulario no cumple con los estandares requeridos")
            if not activos.get("Nombre"):
                nombreActivo = input("Ingrese el nombre del activo: ")
                activos["Nombre"]=nombreActivo
            if not activos.get("Proveedor"):
                activos["Proveedor"]=("Compumax Computer")
            if not activos.get("EmpresaResponsable"):
                activos["EmpresaResponsable"]=("Campuslands")
            if not activos.get("idMarca"):
                print(colors.BOLDYELLOW+"""
                      

                      IDS DE LAS MARCAS


                      1. LG
                      2.COMPUMAX
                      3.LOGITECH
                      4.BENQ
                      5.ASUS
                      6.LENOVO
                      7.HP

"""+colors.RESET)
                idmarca=input("Ingrese el id de la marca: ")

                if(re.match(r'[0-9]+$', idmarca) is not None):
                    activos["idMarca"] = idmarca
                else:
                    raise Exception ("El id de la marca no cumple con los estandares requeridos")
                
            if not activos.get("idCategoria"):
                print(colors.BOLDYELLOW+"""
                      

                    IDS CATEGORIAS DE ACTIVOS
                      
                      1. EQUIPO DE COMPUTO
                      2. ELECTRODOMESTICO
                      3. JUEGO


"""+colors.RESET)
                idcategoria = input("Ingrese el id de la categoria: ")

                if(re.match(r'[0-9]+$', idmarca) is not None):
                    activos["idCategoria"]=idcategoria
                else:
                    raise Exception ("El id de la categoria no cumple con los estandares requeridos")
            if not activos.get("idTipo"):
                print(colors.BOLDYELLOW+"""
                      
                    IDS TIPOS DE ACTIVO
                      
                      1. MONITOR
                      2. CPU
                      3. TECLADO
                      4. MOUSE
                      5. AIRE ACONDICIONADO
                      6. PORTATIL
                      7. TV
                      8. ARCADE

"""+colors.RESET)
                idtipo=input("Ingrese el id del tipo: ")

                if(re.match(r'[0-9]+$', idtipo) is not None):
                    activos["idTipo"]=idtipo
                else:
                    raise Exception ("El id del tipo no cumple con los estandares requeridos")
            if not activos.get("ValorUnitario"):
                valorunitario = input("Ingresa el valor unitario del activo: ")
                if(re.match(r'[0-9]+$', valorunitario) is not None):
                    activos["ValorUnitario"]= valorunitario
                else:
                    raise Exception ("El valor unitario no cumple con los estandares requeridos")
            if not activos.get("idEstado"):
                activos["idEstado"]= str(0)
            if not activos.get("historialActivos"):
                activos["historialActivos"] = []
            if not activos.get("asignaciones"):
                activos["asignaciones"] = []
                
        except KeyboardInterrupt:
            return menuActivos()
        except Exception as error:
            print(error)

        posicion = requests.post("http://154.38.171.54:5502/activos", data=json.dumps(activos, indent=4))
        res = posicion.json
        tablaactivos = [activos]
        return print(tabulate(tablaactivos, headers="keys", tablefmt='rounded_grid'))





def menuActivos():
    while True:
        try:
            print(colors.BOLDYELLOW+"""
                



                            MENU ACTIVOS
                                

                            1. AGREGAR
                            2. EDITAR
                            3. ELIMINAR
                            4. BUSCAR
                            5. REGRESAR AL MENU PRINCIPAL


"""+colors.RESET)
        

            opcion = input("Ingrese una opcion: ")
            if re.match(r'^[1-5]$', opcion) is not None:
                opcion = int(opcion)

            if(opcion==5):
                break
            elif(opcion==1):
                print(tabulate(postActivos(), headers="keys", tablefmt='rounded_grid'))
                print(colors.BOLDYELLOW+"Activo guardado correctamente!"+colors.RESET)
            elif(opcion==2):
                id = input("Ingrese el id de el activo que desea actualizar: ")
                print(tabulate(update(id), headers="keys", tablefmt='rounded_grid'))
                print(colors.BOLDYELLOW+"Activo Editado correctamente!"+colors.RESET)
            elif(opcion==3):
                id = input("Ingrese el id del activo al que desea eliminar el estado: ")
                print(tabulate(deleteactivos(id), headers="keys", tablefmt='rounded_grid'))
                print(colors.BOLDYELLOW+"Activo Eliminado correctamente!"+colors.RESET)
            elif(opcion==4):
                print(tabulate(menubuscar(), headers="keys", tablefmt='rounded_grid'))
        except KeyboardInterrupt:
            break

def getAllActivos():
    activos = []
    for val in getAllDataActivos():
        activos.append({
                        "id": val.get('id'),
                        "NroItem": val.get('NroItem'),
                        "NroSerial": val.get('NroSerial'),
                        "CodCampus": val.get('CodCampus'),
                        "NroFormulario": val.get('NroFormulario'),
                        "Nombre": val.get('Nombre'),
                        "idMarca": val.get('idMarca'),
                        "idCategoria": val.get('idCategoria'),
                        "idTipo": val.get('idTipo'),
                        "ValorUnitario": val.get('ValorUnitario'),
                        "idEstado": val.get('idEstado')
        })
    return activos


def getAllActivosIdCategoria1():
    activos = []
    for val in getAllDataActivos():
        if (val.get("idCategoria")=="1"):
            activos.append({
                        "id": val.get('id'),
                        "NroItem": val.get('NroItem'),
                        "NroSerial": val.get('NroSerial'),
                        "CodCampus": val.get('CodCampus'),
                        "NroFormulario": val.get('NroFormulario'),
                        "Nombre": val.get('Nombre'),
                        "idMarca": val.get('idMarca'),
                        "idCategoria": val.get('idCategoria'),
                        "idTipo": val.get('idTipo'),
                        "ValorUnitario": val.get('ValorUnitario'),
                        "idEstado": val.get('idEstado')
            })
    return activos



def getAllActivosIdCategoria3():
    activos = []
    for val in getAllDataActivos():
        if (val.get("idCategoria")=="3"):
            activos.append({
                        "id": val.get('id'),
                        "NroItem": val.get('NroItem'),
                        "NroSerial": val.get('NroSerial'),
                        "CodCampus": val.get('CodCampus'),
                        "NroFormulario": val.get('NroFormulario'),
                        "Nombre": val.get('Nombre'),
                        "idMarca": val.get('idMarca'),
                        "idCategoria": val.get('idCategoria'),
                        "idTipo": val.get('idTipo'),
                        "ValorUnitario": val.get('ValorUnitario'),
                        "idEstado": val.get('idEstado')
            })
    return activos


def getAllActivosIdCategoria2():
    activos = []
    for val in getAllDataActivos():
        if (val.get("idCategoria")=="2"):
            activos.append({
                        "id": val.get('id'),
                        "NroItem": val.get('NroItem'),
                        "NroSerial": val.get('NroSerial'),
                        "CodCampus": val.get('CodCampus'),
                        "NroFormulario": val.get('NroFormulario'),
                        "Nombre": val.get('Nombre'),
                        "idMarca": val.get('idMarca'),
                        "idCategoria": val.get('idCategoria'),
                        "idTipo": val.get('idTipo'),
                        "ValorUnitario": val.get('ValorUnitario'),
                        "idEstado": val.get('idEstado')
            })
    return activos




def getAllActivos2():
    articulo2 =[]
    for val in getAllDataActivos():
        if (val.get('idEstado') == "2"):
            articulo2.append(
                {
                        "id": val.get('id'),
                        "NroItem": val.get('NroItem'),
                        "NroSerial": val.get('NroSerial'),
                        "CodCampus": val.get('CodCampus'),
                        "NroFormulario": val.get('NroFormulario'),
                        "Nombre": val.get('Nombre'),
                        "idMarca": val.get('idMarca'),
                        "idCategoria": val.get('idCategoria'),
                        "idTipo": val.get('idTipo'),
                        "ValorUnitario": val.get('ValorUnitario'),
                        "idEstado": val.get('idEstado')
                }
            )
    return articulo2





def menubuscar():
    while True:
        print(colors.BOLDYELLOW+"""


                        MENU DE BUSQUEDAS DE ACTIVOS
                                        
                        1. BUSCAR ACTIVOS POR EL ID 
                        2. SALIR

                        -PRESIONE CTRL + C PARA SALIR   

"""+colors.RESET)
        try: 
            
            opcion = input("Ingrese una opcion: ")
            if re.match(r'^[1-2]$', opcion) is not None:
                opcion = int(opcion)

            if(opcion==2):
                break
            elif(opcion==1):
                id = input("Ingrese el id del activo que desea filtrar: ")
                print(tabulate(getAllActivosId(id),headers="keys", tablefmt='rounded_grid'))

        except KeyboardInterrupt:
            break



def update(id):
    while True:

        print(colors.BOLDYELLOW+"""
        
                        QUE INFORMACION DESEA EDITAR
                    
                        1. NroItem
                        2. NroSerial
                        3. CodCampus
                        4. NroFormulario
                        5. Nombre
                        6. idMarca
                        7. idCategoria
                        8. idTipo
                        9. ValorUnitario
                        0. Salir

            -PRESIONE CTRL + C PARA SALIR

    """+colors.RESET)
         
        try:

            activos = {}
            
            opcion = input("Ingrese una opcion: ")
            if re.match(r'^[0-9]$', opcion) is not None:
                opcion = int(opcion)


            if opcion==1:
                    nmeroitem = input("Ingrese el numero de item (SOLO NUMEROS): ")
                    activos["NroItem"] = nmeroitem
            if opcion == 2:
                    numeroserial = input("Ingrese el numero del serial(5-10 CARACTERES ENTRE LETRAS MAYUSCULAS Y NUMEROS): ")
                    activos["NroSerial"]=numeroserial
            if opcion==3:
                codigocampus = input("Ingrese el codigo de campus(5-10 CARACTERES ENTRE LETRAS MAYUSCULAS Y NUMEROS): ")
                activos["CodCampus"]=codigocampus
            if opcion == 4:
                numerofor = input("Ingrese el numero de formulario(SOLO NUMEROS): ")
                activos["NroFormulario"] = numerofor
            if opcion == 5: 
                    nombreActivo = input("Ingrese el nombre del activo: ")
                    activos["Nombre"]=nombreActivo
            if opcion == 6: 
                    print(colors.BOLDYELLOW+"""
        

                      IDS DE LAS MARCAS


                      1. LG
                      2.COMPUMAX
                      3.LOGITECH
                      4.BENQ
                      5.ASUS
                      6.LENOVO
                      7.HP

"""+colors.RESET)
                    idmarca=input("Ingrese el id de la marca: ")
                    if re.match(r'^[0-10]$', idmarca) is not None:
                        activos["idMarca"] = idmarca
            if opcion == 7:
                print(colors.BOLDYELLOW+"""
                      

                    IDS CATEGORIAS DE ACTIVOS
                      
                      1. EQUIPO DE COMPUTO
                      2. ELECTRODOMESTICO
                      3. JUEGO


"""+colors.RESET)
                idcategoria = input("Ingrese el id de la categoria: ")
                if re.match(r'^[0-10]$', idcategoria) is not None:
                    activos["idCategoria"]=idcategoria
            if opcion ==8:
                print(colors.BOLDYELLOW+"""
                      
                    IDS TIPOS DE ACTIVO
                      
                      1. MONITOR
                      2. CPU
                      3. TECLADO
                      4. MOUSE
                      5. AIRE ACONDICIONADO
                      6. PORTATIL
                      7. TV
                      8. ARCADE

"""+colors.RESET)
                idtipo = input("Ingrese el id del tipo: ")

                activos["idTipo"]=idtipo
            if opcion == 9:
                valorunitario = input("Ingresa el valor unitario del activo: ")
                activos["ValorUnitario"]= valorunitario
            if opcion ==8: 
                break
        
        except KeyboardInterrupt:
            break


        activoexistente = getActivosId(id)
        if not activoexistente:
            return {"Mensaje": "Activo no encontrado"}
        activoactualizado = {**activoexistente[0], **activos}
        peticion = requests.put(f'http://154.38.171.54:5502/activos/{id}', data=json.dumps(activoactualizado, indent=4))
        res = peticion.json()
        tablaactualuzar = [activos]
        print("Activo Editado Correctamente :) ")
        return 
        
