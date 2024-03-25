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
                nmeroitem = int(input("Ingrese el numero de item: "))
                activos["NroItem"] = nmeroitem
            # else:
            #         raise Exception ("El numero de item no cumple con los estandares requeridos")
                
            if not activos.get("CodTransaccion"):

                activos["CodTransaccion"]=327
            # else:
            #         raise Exception ("El codigo de transaccion no cumple con los estandares requeridos")
            if not activos.get("NroSerial"):
                numeroserial = input("Ingrese el numero del serial: ")
                if(re.match(r"^[A-Z0-9-]{5,10}$", numeroserial)is not None):
                    activos["CodTransaccion"]=numeroserial
                else:
                    raise Exception ("El numero del serial no cumple con los estandares requeridos")
            if not activos.get("CodCampus"):
                codigocampus = input("Ingrese el codigo de campus: ")
                if(re.match(r"^[A-Z0-9-]{5,10}$", numeroserial)is not None):
                    activos["CodCampus"]=codigocampus
                else:
                    raise Exception ("El codigo de campus no cumple con los estandares requeridos")
            if not activos.get("NroFormulario"):
                numerofor = int(input("Ingrese el numero de formulario: "))

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
                idmarca=int(input("Ingrese el id de la marca: "))
                activos["idMarca"] = idmarca
            if not activos.get("idCategoria"):
                idcategoria = int(input("Ingrese el id de la categoria: "))
                activos["idCategoria"]=idcategoria
            if not activos.get("idTipo"):
                idtipo=int(input("Ingrese el id del tipo: "))
                activos["idTipo"]=idtipo
            if not activos.get("ValorUnitario"):
                valorunitario = int(input("Ingresa el valor unitario del activo: "))
                activos["ValorUnitario"]= valorunitario
            if not activos.get("idEstado"):
                activos["idEstados"]= int(0)
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
                    idmarca=int(input("Ingrese el nuevo id de la marca: "))
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

        activoexistente = getAllDataActivos()
        if not activoexistente:
            return {"Mensaje": "Activo no encontrado"}
        
        activoactualizado = {**activoexistente[0], **activos}
        peticion = requests.put(f'http://154.38.171.54:5502/activos{id}', data=json.dumps(activoactualizado))
        res = peticion.json()

        if peticion.status_code == 200:
            res["Mensaje"] =  "Activo actualizado correctamente"
        else: 
            res["Mensaje"] = "Error al actualizar activos"
        return[res]

def deleteactivos(id):
     print("""
           

                TIPOS DE ESTADOS DE UN ACTIVO
           

                        
                0. No asignado
                1. Asignado 
                2. Dado de baja por daño 
                3. En reparación y/o garantia

           
""")
     activos = {
          "idEstado": int(input("Ingrese el estado al que desea cambiar el activo: "))
     }
     
     activo_encontrado = getActivosId(id)
     if not activo_encontrado:
          return {"Mensaje": "Activo no encontrado"}
     Activoactualizado = {**activo_encontrado[0], **activos}
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
            id = input("Ingrese el id del activo al que desea actualizarle el estado: ")
            print(deleteactivos(id))