from tabulate import tabulate
import modules.postActivos as activos
import modules.postAsignaciones as asignaciones






def ActivosCategoria():
    while True:
        print("""
              
                                        
                            CATEGORIAS
                                        
                            1. EQUIPO DE COMPUTO
                            2. ELECTRODOMESTICO
                            3. JUEGO
                            0. SALIR
                                        


""")
        opcion = int(input("Ingrese la opcion que desea flitrar: "))
        if(opcion!=1) and (opcion!=2) and (opcion!=3) and (opcion!=0):
            print("Opcion no existente!")
            print("Intente nuevamente :)")
        if(opcion==0):
            break
        elif(opcion==1):
            print(tabulate(activos.getAllActivosIdCategoria1(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==2):
            print(tabulate(activos.getAllActivosIdCategoria2(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==3):
            print(tabulate(activos.getAllActivosIdCategoria3(), headers="keys", tablefmt='rounded_grid'))

        




def MenuRepores():
    while True:
        print("""

                                    MENU REPORTES
                                                
                                    1. LISTAR TODOS LOS ACTIVOS
                                    2. LISTAR ACTIVOS POR CATEGORIA
                                    3. LISTAR ACTIVOS DADOS DE BAJA POR DAÑO
                                    4. LISTAR ACTIVOS Y ASIGNACION
                                    5. LISTAR HISTORIAL DE MOV. DE ACTIVO
                                    6. REGRESAR AL MENU PRINCIPAL

""")
        
        opcion = int(input("Ingrese la opcion deseada: "))
        if(opcion!=1) and (opcion!=2) and (opcion!=3) and (opcion!=4) and (opcion!=5) and (opcion!=6):
            print("Opcion no existente!")
            print("Intente nuevamente :)")
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