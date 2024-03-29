from tabulate import tabulate
import modules.postActivos as activos






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
        if opcion==6:
            break
        elif(opcion==1):
            print(tabulate(activos.getAllActivos(), headers="keys", tablefmt='rounded_grid'))
        elif(opcion==2):
            ActivosCategoria()
        elif(opcion==3):
            print(tabulate(activos.getAllActivos2(), headers="keys", tablefmt='rounded_grid'))