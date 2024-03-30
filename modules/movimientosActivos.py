import modules.postActivos as activ
import requests
import json


def menuMoviActivos():
    while True:
        print("""

                        MENU MOVIMIENTO DE ACTIVOS
                                    
                                    
                        1. RETORNO DE ACTIVO
                        2. DAR DE BAJA ACTIVO
                        3. CAMBIAR ASIGNACION DE ACTIVO
                        4. ENVIAR A GARANTIA ACTIVO
                        5. REGRESAR AL MENU PRINCIPAL

""")
        
        opcion = input("Ingrese la opcion deseada: ")
        if opcion not in [1,2,3,4,5]:
            print("opcion no encontrada")
            print("Intente nuevamente :)")
            menuMoviActivos()
        if opcion==5:
            break
        


