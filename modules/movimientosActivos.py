import modules.postActivos as activ
import requests
import json
from tabulate import tabulate
import os
class colors:
    RESET = '\033[0m'
    BOLDYELLOW = '\033[1;33m'


def menuMoviActivos():
    while True:
        os.system("clear")
        print(colors.BOLDYELLOW+"""

                        MENU MOVIMIENTO DE ACTIVOS
                                    
                                    
                        1. RETORNO DE ACTIVO
                        2. DAR DE BAJA ACTIVO
                        3. CAMBIAR ASIGNACION DE ACTIVO
                        4. ENVIAR A GARANTIA ACTIVO5
                        5. REGRESAR AL MENU PRINCIPAL
                PRECIONE CTRL + C PARA SALIR DEL MENU PRINCIPAL
"""+colors.RESET)
        try: 
            opcion = input("Ingrese una opcion: ")
            if re.match(r'^[1-5]$', opcion) is not None:
                opcion = int(opcion)

                menuMoviActivos()
            if opcion==5:
                break
            elif opcion == 1:
                id = input("Ingrese el id del activo que desea restaurar: ")
                print(tabulate(activ.cambiarEstadoa0(id)))
            elif opcion==2:
                id = input("Ingrese el id del activo que desea dar de baja: ")
                print(tabulate(activ.cambiarEstadoa2(id)))
            elif opcion ==4:
                id = input("Ingrese el id del activo que desea mandar a garantia: ")
                print(tabulate(activ.cambiarEstadoa3(id)))
            elif opcion ==3:
                id = input("Ingrese el id del activo que desea reasignar: ")
                print(tabulate(activ.reasignar(id)))
        except KeyboardInterrupt:
            break
