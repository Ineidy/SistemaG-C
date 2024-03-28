from tabulate import tabulate
import modules. postActivos as activos










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