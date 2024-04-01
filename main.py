import modules.postAsignaciones as postasigna
import modules.postPersonal as postpersonal
import modules.postActivos as postActivos
import modules.postZonas as postZonas
import modules.postReportes as postreportes
import modules.movimientosActivos as movimientos
import os
import re

class colors:
    RESET = '\033[0m'
    BOLDYELLOW = '\033[1;33m'


if(__name__=='__main__'):

    while True:
        os.system("clear")

        print(colors.BOLDYELLOW + """



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
                -PRESIONA CTROL + C PARA SALIR DEL PROGRAMA
                                    
"""+ colors.RESET) 
        try: 
            opcion = input("Ingrese una opcion: ")
            if re.match(r'^[1-7]$', opcion) is not None:
                opcion = int(opcion)
            else:
                break

            if (opcion==1):
                postActivos.menuActivos()
            elif(opcion==2):
                postpersonal.menuPersonal()
            elif(opcion==3):
                postZonas.menuzonas()
            elif(opcion==4):
                postasigna.menuAsignacionActivos()
            elif(opcion==5):
                postreportes.MenuRepores()
            elif(opcion==6):
                movimientos.menuMoviActivos()
            elif(opcion==7):
                break
        
        except KeyboardInterrupt:
            break