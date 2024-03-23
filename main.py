import re
import modules.getActivos as getActivos
import modules.getAsignaciones as getasigna
import modules.getPersonas as getperson
import modules.getReportes as getreport
import modules.getTipMovActivos as gettiposmovimientosactivos
import modules.getZonas as getzonas
import modules.postZonas as postZonas




if(__name__=='__main__'):

    while True:

        print("""



   _____ _______________________  ______       _________    ______                                                                   
  / ___//  _/ ___/_  __/ ____/  |/  /   |     / ____( _ )  / ____/                                                                   
  \__ \ / / \__ \ / / / __/ / /|_/ / /| |    / / __/ __ \// /                                                                        
 ___/ // / ___/ // / / /___/ /  / / ___ |   / /_/ / /_/  < /___                                                                      
/____/___//____//_/ /_____/_/  /_/_/  |_|   \____/\____/\|____/                                                                      
   / __ \/ ____/                                                                                                                     
  / / / / __/                                                                                                                        
 / /_/ / /___                                                                                                                        
/_____/_____/__    _________   ___________    ____  ________     _________    __  _______  __  _______ __    ___    _   ______  _____
   /  _/ | / / |  / / ____/ | / /_  __/   |  / __ \/  _/ __ \   / ____/   |  /  |/  / __ \/ / / / ___// /   /   |  / | / / __ \/ ___/
   / //  |/ /| | / / __/ /  |/ / / / / /| | / /_/ // // / / /  / /   / /| | / /|_/ / /_/ / / / /\__ \/ /   / /| | /  |/ / / / /\__ \ 
 _/ // /|  / | |/ / /___/ /|  / / / / ___ |/ _, _// // /_/ /  / /___/ ___ |/ /  / / ____/ /_/ /___/ / /___/ ___ |/ /|  / /_/ /___/ / 
/___/_/ |_/  |___/_____/_/ |_/ /_/ /_/  |_/_/ |_/___/\____/   \____/_/  |_/_/  /_/_/    \____//____/_____/_/  |_/_/ |_/_____//____/  



                                                                                                
        OPCIONES


        1. ACTIVOS
        2. PERSONAL
        3. ZONAS
        4. ASIGNACION DE ACTIVOS
        5. REPORTES
        6. MOVIMIENTO DE ACTIVOS
        7. SALIR
                
""")
        opcion = int(input("Ingrese una opcion: "))
        if (opcion==1):
            getActivos.menuActivos()
        elif(opcion==2):
            getperson.menuPersonal()
        elif(opcion==3):
            postZonas.menuzonas()
        elif(opcion==4):
            getasigna.menuAsignacionActivos()
        elif(opcion==5):
            getreport.menuReportes()
        elif(opcion==6):
            gettiposmovimientosactivos.menuMovimientosActivos()
        elif(opcion==7):
            break
