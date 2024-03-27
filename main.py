import re

import modules.getAsignaciones as getasigna
import modules.postPersonal as postpersonal
import modules.getReportes as getreport
import modules.getTipMovActivos as gettiposmovimientosactivos
import modules.postActivos as postActivos
import modules.postZonas as postZonas
import json



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
        if(opcion!=1) and (opcion!=2) and (opcion!=3) and (opcion!=4) and (opcion!=5) and (opcion!=6) and (opcion!=7):
            print("Opcion no existente!")
            print("Intente nuevamente :)")
            (__name__=='__main__')
        if (opcion==1):
            postActivos.menuActivos()
        elif(opcion==2):
            postpersonal.menuPersonal()
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







# with open("storage/zonas.json", "r") as f:
#     fichero = f.read()
#     data = json.loads(fichero)
#     for i, val in enumerate(data):
#         data[i]["id"] = (i+1)
#     data = json.dumps(data, indent=4).encode("utf-8")
#     with open("storage/zonas.json", "wb+") as f1:
#         f1.write(data)
#         f1.close()