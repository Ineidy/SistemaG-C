import requests
import re
import json
from tabulate import tabulate

def getAllDataActivos():
    peticionactivos = requests.get("http://154.38.171.54:5502/activos")
    dataactivos = peticionactivos.json()
    return dataactivos

def getActivosId(id):
    peticion= requests.get(f"http://154.38.171.54:5502/activos/{id}")
    return[peticion.json()] if peticion.ok else []

def postActivos():

    while True:
        activos = {}
        try:

            if not activos.get("NroItem"):
                nmeroitem = input("Ingrese el numero de item: ")
                if(re.match(r'[0-9]+$', nmeroitem) is not None):
                    nmeroitem = int(nmeroitem)
                activos["NroItem"] = nmeroitem
            else:
                    raise Exception ("El numero de item no cumple con los estandares requeridos")
                
            if not activos.get("CodTransaccion"):
                activos["CodTransaccion"]=int(327)
            # else:
            #         raise Exception ("El codigo de transaccion no cumple con los estandares requeridos")
            if not activos.get("NroSerial"):
                numeroserial = input("Ingrese el numero del serial: ")
                if(re.match(r"^[A-Z0-9]{5,10}$", numeroserial)is not None):
                    activos["NroSerial"]=numeroserial
                else:
                    raise Exception ("El numero del serial no cumple con los estandares requeridos")
            if not activos.get("CodCampus"):
                codigocampus = input("Ingrese el codigo de campus: ")
                if(re.match(r"^[A-Z0-9-]{5,10}$", numeroserial)is not None):
                    activos["CodCampus"]=codigocampus
                else:
                    raise Exception ("El codigo de campus no cumple con los estandares requeridos")
            if not activos.get("NroFormulario"):
                numerofor = input("Ingrese el numero de formulario: ")
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
                idmarca=input("Ingrese el id de la marca: ")
                if(re.match(r'[0-9]+$', idmarca) is not None):
                    activos["idMarca"] = idmarca
                else:
                    raise Exception ("El id de la marca no cumple con los estandares requeridos")
                
            if not activos.get("idCategoria"):
                idcategoria = input("Ingrese el id de la categoria: ")
                if(re.match(r'[0-9]+$', idmarca) is not None):
                    activos["idCategoria"]=idcategoria
                else:
                    raise Exception ("El id de la categoria no cumple con los estandares requeridos")
            if not activos.get("idTipo"):
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
                activos["idEstados"]= str(0)
            if not activos.get("historialActivos"):
                activos["historialActivos"] = []
            if not activos.get("asignaciones"):
                activos["asignaciones"] = []
                
        except Exception as error:
            print(error)

        posicion = requests.post("http://154.38.171.54:5502/activos", data=json.dumps(activos, indent=4))
        res = posicion.json
        tablaactivos = [activos]
        return print(tabulate(tablaactivos, headers="keys", tablefmt='rounded_grid'))

def update(id):
    activos ={}
    while True:
        try:
            print("""
        
            QUE INFORMACION DESEA EDITAR
        
            1. NroItem
            2. CodTransaccion
            3. NroSerial
            4. CodCampus
            5. NroFormulario
            6. Nombre
            7. idMarca
            8. idCategoria
            9. idTipo
            10. ValorUnitario


""")
            
            opcion = int(input("Ingrese la opcion deseada: "))
            if(opcion!=1) and (opcion!=2) and (opcion!=3) and (opcion!=4) and (opcion!=5) and (opcion!=6) and (opcion!=7) and (opcion!=8) and (opcion!=9) and (opcion!=10):
                print("Opcion no existente!")
                print("Intente nuevamente :)")
                update(id)
            if(opcion==1):
                nmeroitem = int(input("Ingrese el nuevo numero de item: "))
                activos["NroItem"] = nmeroitem
            if(opcion==2):
                codigotransaccion = int(input("Ingrese el nuevo codigo de la transaccion: "))
                activos["CodTransaccion"]=codigotransaccion
            if(opcion==3):

                    numeroserial = input("Ingrese el nuevo numero del serial: ")
                    if(re.match(r"^[A-Z0-9-]{5,10}$", numeroserial)is not None):
                        activos["CodTransaccion"]=numeroserial
                    else:
                        raise Exception ("El numero del serial no cumple con los estandares requeridos")
            if(opcion==4):

                    codigocampus = input("Ingrese el nuevo codigo de campus: ")
                    if(re.match(r"^[A-Z0-9-]{5,10}$", numeroserial)is not None):
                        activos["CodCampus"]=codigocampus
                    else:
                        raise Exception ("El codigo de campus no cumple con los estandares requeridos")
            if(opcion==5):
                    numerofor = int(input("Ingrese el nuevo numero de formulario: "))
                    activos["NroFormulario"]=numerofor
            if(opcion==6):
                    nombreActivo = input("Ingrese el nuevo nombre del activo: ")
                    activos["Nombre"]=nombreActivo
            if(opcion==7):
                    idmarca=input("Ingrese el nuevo id de la marca: ")
                    activos["idMarca"] = idmarca
            if(opcion==8):
                    idcategoria = int(input("Ingrese el id de la categoria: "))
                    activos["idCategoria"]=idcategoria
            if(opcion==9):
                    idtipo=int(input("Ingrese el id del tipo: "))
                    activos["idTipo"]=idtipo
            if(opcion==10):
                    valorunitario = int(input("Ingresa el valor unitario del activo: "))
                    activos["ValorUnitario"]= valorunitario

        except Exception as error:
            print(error)

        activoexistente = getActivosId(id)
        if not activoexistente:
            return {"Mensaje": "Activo no encontrado"}
        
        activoactualizado = {**activoexistente[0], **activos}
        peticion = requests.put(f'http://154.38.171.54:5502/activos/{id}', data=json.dumps(activoactualizado))
        res = peticion.json()

        if peticion.status_code == 200:
            res["Mensaje"] =  "Activo actualizado correctamente"
        else: 
            res["Mensaje"] = "Error al actualizar activos"
        return res

def deleteactivos(id):

    activo_encontrado = getActivosId(id)
    if not activo_encontrado:
        return {"Mensaje": "Activo no encontrado"}
    Activoactualizado = {**activo_encontrado[0], "idEstado": "2"}
    peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(Activoactualizado))
    res = peticion.json()

    if peticion.status_code == 200:
        res["Mensaje"] = "Estado actualizado correctamente!"
    else: 
        res["Mensaje"] = "Error en la actualizacion del estado!"
    return [res]

    


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
        if(opcion!=1) and (opcion!=2) and (opcion!=3) and (opcion!=4) and (opcion!=5):
            print("Opcion no existente!")
            print("Intenta nuevamente :)")
        elif(opcion==5):
            break
        elif(opcion==1):
            print(tabulate(postActivos(), headers="keys", tablefmt='rounded_grid'))
            print("Activo guardado correctamente!")
        elif(opcion==2):
            id = input("Ingrese el id de el activo que desea actualizar: ")
            print(tabulate(update(id), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==3):
            id = input("Ingrese el id del activo al que desea eliminar el estado: ")
            print(tabulate(deleteactivos(id), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==4):
            print(tabulate(menubuscar(), headers="keys", tablefmt='rounded_grid'))

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


def getAllArticulos0():
    articulo =[]
    for val in getAllDataActivos():
        if (val.get("idEstado") == "0"):
            articulo.append(
                {
                        "NroItem": val.get('NroItem'),
                        "NroFormulario": val.get('NroFormulario'),
                        "Nombre": val.get('Nombre'),
                        "idEstado": val.get('idEstado')
                }
            )
    return articulo

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

def getAllArticulos1():
    articulo1 =[]
    for val in getAllDataActivos():
        if (val.get("idEstado") == "1"):
            articulo1.append(
                {
                        "NroItem": val.get('NroItem'),
                        "NroFormulario": val.get('NroFormulario'),
                        "Nombre": val.get('Nombre'),
                        "idEstado": val.get('idEstado')
                }
            )
    return articulo1

def getAllArticulos3():
    articulo3 =[]
    for val in getAllDataActivos():
        if (val.get("idEstado") == "3"):
            articulo3.append(
                {
                        "NroItem": val.get('NroItem'),
                        "NroFormulario": val.get('NroFormulario'),
                        "Nombre": val.get('Nombre'),
                        "idEstado": val.get('idEstado')
                }
            )
    return articulo3


def getAllArticulos2():
    articulo2 =[]
    for val in getAllDataActivos():
        if (val.get('idEstado') == "2"):
            articulo2.append(
                {
                        "NroItem": val.get('NroItem'),
                        "NroFormulario": val.get('NroFormulario'),
                        "Nombre": val.get('Nombre'),
                        "idEstado": val.get('idEstado')
                }
            )
    return articulo2

def getAllActivosItem(item):
    activosItem = []
    for val in getAllDataActivos():
        if(val.get('NroItem') == item):
            activosItem.append({
                    "NroItem": val.get('NroItem'),
                    "NroFormulario": val.get('NroFormulario'),
                    "Nombre": val.get('Nombre'),
                    "idEstado": val.get('idEstado')
            })
    return activosItem

def getAllActivosValorU(valorU):
    activosvalor=[]
    for val in getAllDataActivos():
        if(val.get('ValorUnitario') == valorU):
            activosvalor.append({
                    "NroItem": val.get('NroItem'),
                    "NroFormulario": val.get('NroFormulario'),
                    "Nombre": val.get('Nombre'),
                    "idEstado": val.get('idEstado'),
                    "valorUnitario": val.get('ValorUnitario')
            })
    return activosvalor

def getAllActivosIdCategoria(idcate):
    activosidcate=[]
    for val in getAllDataActivos():
        if(val.get('idCategoria') == idcate):
            activosidcate.append({
                    "NroItem": val.get('NroItem'),
                    "NroFormulario": val.get('NroFormulario'),
                    "Nombre": val.get('Nombre'),
                    "idEstado": val.get('idEstado'),
                    "valorUnitario": val.get('ValorUnitario'),
                    "idCategoria": val.get('idCategoria')
            })
    return activosidcate


def getAllActivosIdTipo(idtipo):
    activosidtipo=[]
    for val in getAllDataActivos():
        if(val.get('idTipo') == idtipo):
            activosidtipo.append({
                    "NroItem": val.get('NroItem'),
                    "NroFormulario": val.get('NroFormulario'),
                    "Nombre": val.get('Nombre'),
                    "idEstado": val.get('idEstado'),
                    "valorUnitario": val.get('ValorUnitario'),
                    "idTipo": val.get('idTipo')
            })
    return activosidtipo

def getAllActivosIdMarca(idmarca):
    activosidmarca=[]
    for val in getAllDataActivos():
        if(val.get('idTipo') == idmarca):
            activosidmarca.append({
                    "NroItem": val.get('NroItem'),
                    "NroFormulario": val.get('NroFormulario'),
                    "Nombre": val.get('Nombre'),
                    "idEstado": val.get('idEstado'),
                    "valorUnitario": val.get('ValorUnitario'),
                    "idMarca": val.get('idMarca')
            })
    return activosidmarca




def menubuscar():
    while True:
        print("""


                        MENU DE BUSQUEDAS DE ACTIVOS
                                        
                        1. BUSCAR ACTIVOS NO ASIGNADOS
                        2. BUSCAR ACTIVOS ASIGNADOS
                        3. BUSCAR ACTIVOS DADOS DE BAJA POR DAÑO
                        4. BUSCAR ACTIVOS EN REPARACION Y/O GARANTIA
                        5. BUSCAR ACTIVOS POR EL ID 
                        6. BUSCAR ACTIVOS POR EL NUMERO DE ITEM
                        7. BUSCRA ACTIVO POR EL VALOR UNITARIO
                        8. BUSCAR ACTIVO POR ID DE CATEGORIA
                        9. BUSCAR ACTIVO POR ID DE TIPO
                        10. BUSCAR ACTIVO POR ID DE LA MARCA
                        0. SALIR
                                        

""")
        
        opcion = int(input("Ingrese la opcion que desea filtrar: "))
        if(opcion!=1) and (opcion!=2) and (opcion!=3) and (opcion!=4)and (opcion!=5)and (opcion!=6)and (opcion!=7)and (opcion!=8)and (opcion!=9)and (opcion!=10)and (opcion!=0):
            print("Opcion no existente!")
            print("Intenta nuevamente :)")
            menubuscar()

        if(opcion==0):
            break
        elif(opcion==1):
            print(tabulate(getAllArticulos0(),headers="keys", tablefmt='rounded_grid'))
        elif(opcion==2):
            print(tabulate(getAllArticulos1(),headers="keys", tablefmt='rounded_grid'))
        elif(opcion==3):
            print(tabulate(getAllArticulos2(),headers="keys", tablefmt='rounded_grid'))
        elif(opcion==4):
            print(tabulate(getAllArticulos3(),headers="keys", tablefmt='rounded_grid'))
        elif(opcion==5):
            id = input("Ingrese el id del activo que desea filtrar: ")
            print(tabulate(getActivosId(id),headers="keys", tablefmt='rounded_grid'))
        elif(opcion==6):
            item = int(input("Ingrese el numero del item que desea filtrar: "))
            print(tabulate(getAllActivosItem(item),headers="keys", tablefmt='rounded_grid'))
        elif(opcion==7):
            valorU = input("Ingrese el valor unitario que desea filtrar: ")
            print(tabulate(getAllActivosValorU(valorU),headers="keys", tablefmt='rounded_grid'))
        elif(opcion==8):
            idcate = input("Ingrese el id de la categoria que desea filtrar: ")
            print(tabulate(getAllActivosIdCategoria(idcate),headers="keys", tablefmt='rounded_grid'))
        elif(opcion==9):
            idtipo = input("Ingrese el id del tipo que desea filtrar: ")
            print(tabulate(getAllActivosIdTipo(idtipo),headers="keys", tablefmt='rounded_grid'))
        elif(opcion==10):
            idmarca = input("Ingrese el id de la marca que desea filtrar: ")
            print(tabulate(getAllActivosIdMarca(idmarca),headers="keys", tablefmt='rounded_grid'))
