
def menuReportes():
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
        opcion = int(input("Ingrese una opcion: "))

        if(opcion==6):
            break
