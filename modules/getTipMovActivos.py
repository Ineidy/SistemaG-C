import requests

# json.server storage/tipoMovActivos.json -b 5007
def getDataMovActiv():
    peticion = requests.get("")
    data = peticion.json()
    return data


def menuMovimientosActivos():
    while True:
        print("""

              


        MENU MOVIMIENTO DE ACTIVOS
                    
                    
        1. RETORNO DE ACTIVO
        2. DAR DE BAJA ACTIVO
        3. CAMBIAR ASIGNACION DE ACTIVO
        4. ENVIAR A GARANTIA ACTIVO
        5. REGRESAR AL MENU PRINCIPAL

""")
        
        opcion = int(input("Ingrese una opcion: "))

        if(opcion==5):
            break

