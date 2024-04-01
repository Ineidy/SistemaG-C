from tabulate import tabulate
import modules.postActivos as activos
import modules.postAsignaciones as asignaciones
import re



class colors:
    RESET = '\033[0m'
    BOLDYELLOW = '\033[1;33m'


def ActivosCategoria():
    while True:
        try:
            print(colors.BOLDYELLOW+"""
              
                                        
                            CATEGORIAS
                                        
                            1. EQUIPO DE COMPUTO
                            2. ELECTRODOMESTICO
                            3. JUEGO
                            0. SALIR

        -SI QUIERE SALIR DE UNA OPCION QUE SELECCIONO, PRESIONE CTROL + C PARA CANCELAR OPCION  


"""+colors.RESET)
            opcion = input("Ingrese una opcion: ")
            if re.match(r'^[0-3]$', opcion) is not None:
                opcion = int(opcion)
            if(opcion==0):
                break
            elif(opcion==1):
                print(tabulate(activos.getAllActivosIdCategoria1(), headers="keys", tablefmt='rounded_grid'))
            elif(opcion==2):
                print(tabulate(activos.getAllActivosIdCategoria2(), headers="keys", tablefmt='rounded_grid'))
            elif(opcion==3):
                print(tabulate(activos.getAllActivosIdCategoria3(), headers="keys", tablefmt='rounded_grid'))

        except KeyboardInterrupt:
            break
        




def MenuRepores():
    while True:
        try: 
            print(colors.BOLDYELLOW+"""

                                    MENU REPORTES
                                                
                                    1. LISTAR TODOS LOS ACTIVOS
                                    2. LISTAR ACTIVOS POR CATEGORIA
                                    3. LISTAR ACTIVOS DADOS DE BAJA POR DAÑO
                                    4. LISTAR ACTIVOS Y ASIGNACION
                                    5. LISTAR HISTORIAL DE MOV. DE ACTIVO
                                    6. REGRESAR AL MENU PRINCIPAL

        -SI QUIERE SALIR DE UNA OPCION QUE SELECCIONO, PRESIONE CTROL + C PARA CANCELAR OPCION
"""+colors.RESET)
            
            opcion = input("Ingrese una opcion: ")
            if re.match(r'^[1-6]$', opcion) is not None:
                opcion = int(opcion)
            if opcion==6:
                break
            elif(opcion==1):
                print(tabulate(activos.getAllActivos(), headers="keys", tablefmt='rounded_grid'))
            elif(opcion==2):
                ActivosCategoria()
            elif(opcion==3):
                print(tabulate(activos.getAllActivos2(), headers="keys", tablefmt='rounded_grid'))
            elif(opcion==4):
                id = input("Ingrese el id de el activo que desea buscar las asiganciones: ")
                print(tabulate(asignaciones.getAllAsignaId(id), headers="keys", tablefmt='rounded_grid'))
            elif opcion==5:
                id = input("Ingrese el id del activo del que desea bucar el historial")
                print(tabulate(asignaciones.getAllHistorialId(id), headers="keys", tablefmt='rounded_grid'))
        except KeyboardInterrupt:
            break