import requests
# json-server storage/asignaciones.json -b 5002
def getDataAsignaciones():
    peticionAsignaciones = requests.get("http://192.168.1.117:5002")
    dataAsignaciones = peticionAsignaciones.json()
    return dataAsignaciones



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



