Explicacion De El Codigo, para que el usuario entenda como usarlo facilmente :)

Al iniciar en el menu:
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/007150d2-bc02-4486-8342-6575563cbda8)
aqui el codigo nos permite ingresar un numero del 1 al 7, que cada uno de estos numeros nos lleba a una funcion distinta,
a continuancion explicare que funcion cumple cada una de ellas:}

ACTIVOS:
al seleccionar la opcion 1 de el menu principal Nos lleva a: 
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/85acd4bb-eee6-4031-b3c4-606257c8c0a5)
la cual nos da las opciones de Agregar, Editar, Eliminar, Buscar y salir, pasa lo mismo que en el menu principal 
y es que el codigo nos permite ingresar un numero del 1 al 5, que cada numero nos dirige a como indica su nombre, 
Agregar, Editar, Eliminar, Buscar Activos y a salir del menu.

 ACTIVOS __ AGREGAR:
 ![image](https://github.com/Ineidy/proyectoPython/assets/160775201/f41a7343-7fa7-4e7f-a02f-12ae422a3b57)
 ![image](https://github.com/Ineidy/proyectoPython/assets/160775201/281077c7-2ad1-4288-9088-fe513e449316)
 ![image](https://github.com/Ineidy/proyectoPython/assets/160775201/d4ae817c-e653-4cc7-bb08-567909bbfc70)

 al seleccionar la opcion 1 de el menu de ACTIVOS, nos lleva a la opcion de Agregar, en donde nos pide cierta informacion 
 para agrearae un activo, esta informacion viene esfecificada de el como o con que tipo de dato se quiene que llenar
si los datos dados son correctos, el activo se guardara en la base de datos
 
  ACTIVOS __ EDITAR: 
  ![image](https://github.com/Ineidy/proyectoPython/assets/160775201/1dfc1a26-124f-4e2b-b5a8-f36b745592ac)
  ![image](https://github.com/Ineidy/proyectoPython/assets/160775201/1b80e28d-7587-4769-a920-dca78209a206)

 Al seleccionar la opcion 2 del menu de activos, nos lleva a editar, donde principalmente, nos pide el id de el activo que
 deseamos eliminar, (Si el id no existe, despues de intentar editar un dato, nos manda una tabla que nos dice que el activo
 no fue encontrado y nos devuelve al menu de activos), si el codigo existe, nos deja seleccionar la informacion que queremos
 editar, y nuevamente nos permite agregar la informacion, y guardarla en el servidor.

 ACTIVOS __ ELIMINAR: 
 ![image](https://github.com/Ineidy/proyectoPython/assets/160775201/0fc4ea45-b45d-41b0-9c27-1b2c49b65479)
 
 Al seleccionar la opcion 3 del menu de ACTIVOS, nos lleva a la opcion de eliminar, donde nos pide el id de un activo,
 si el id existe, cambia el estado de el activo a 2 (Dado de baja), y crea un historial de activos que contienen nroId, 
 fecha(Del dia que se elimino el activo), tipoMov (En este caso el 2) y el idRespMov(valindando si la persona existe, y 
 y si no, no permite eliminar activo).

 ACTIVOS __BUSCAR:
 ![image](https://github.com/Ineidy/proyectoPython/assets/160775201/5d324c3d-ba97-4439-acd5-1d96f05738a5)

 al seleccionar la opcion 4 del Menu de activos, nos lleva a la opcion de buscar, donde nos permite 1. buscar activo por el id 
 2. Salir(volver al menu anterior, si esa opcion es seleccionada), si seleccionamos la opcion de buscar activo nos permite 
 introducir el id de el activo que queremos buscar, y nos retorna informacion sobre el activo buscado si es que existe.

ACTIVOS __ REGRESAR AL MENU PRINCIPAL:

al seleccionar la opcion 5, el menu se retrocedera al anterior menu

PERSONAS
al seleccionar la opcion 2 de el menu principal Nos lleva a: 
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/a3dd9b1a-ed39-42fe-820d-8d68df4ec571)

la cual nos da las opciones de Agregar, Editar, Eliminar, Buscar y salir, pasa lo mismo que en el menu principal 
y es que el codigo nos permite ingresar un numero del 1 al 5, que cada numero nos dirige a como indica su nombre, 
Agregar, Editar, Eliminar, Buscar Activos y a salir de los datos de la persona.

PERSONAS __ AGREGAR:
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/fd3c40b9-cd5f-4c49-98d0-308abc020dc2)

 al seleccionar la opcion 1 de el menu de personas, nos lleva a la opcion de Agregar, en donde nos pide cierta informacion 
 para agreara una persona nueva a la base de datos, esta informacion viene esfecificada de el como o con que tipo de dato se quiene que llenar
si los datos dados son correctos, la persona se guardara en la base de datos.

PERSONAS __ EDITAR: 
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/98a3f47b-94ae-46e9-a199-152ed277f19a)

![image](https://github.com/Ineidy/proyectoPython/assets/160775201/de4ec9db-aef6-43c9-9d52-76c5d8d6d634)

 Al seleccionar la opcion 2 del menu de personas, nos lleva a editar, donde principalmente, nos pide el id de la persona que
 deseamos eliminar, (Si el id no existe, despues de intentar editar un dato, nos manda una tabla que nos dice que la persona
 no fue encontrado y nos devuelve al menu de personas), si el codigo existe, nos deja seleccionar la informacion que queremos
 editar, y nuevamente nos permite agregar la informacion, y guardarla en el servidor.

PERSONA __ ELIMINAR:
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/bed812ee-22f0-475e-84cb-2bbbaa4ea3c6)

 
 Al seleccionar la opcion 3 del menu de Personas, nos lleva a la opcion de eliminar, donde nos pide el id de una persona.
 si el id existe, elimina a la persona totalmente de la base de datos.

 PERSONAS __ BUSCAR
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/7f05ea06-f124-43be-8756-4ca7ed191d4d)

 al seleccionar la opcion 4 del Menu de personas, nos lleva a la opcion de buscar, donde nos permite 1. buscar persona por el id 
 2. Buscar persona por el nrdId, 3. buscar persona por el nombre, 4. buscar persona por el email, 0. Salir(volver al menu anterior, si esa opcion es seleccionada),
 cada una de estas opciones nos permite buscar dentro de la base de datos la informacion de la persona que el usuiario introdujo.

 PERSONAS __ REGRESAR AL MENU PRINCIPAL:

al seleccionar la opcion 5, el menu se retrocedera al anterior menu


ZONAS:
al seleccionar la opcion 3 de el menu principal Nos lleva a: 
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/3a1f54a2-e767-4eb2-972a-bcfc296f1081)

ZONAS __ AGREGAR:
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/32d471cd-c15a-4887-bd35-0c644e4568fb)
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/056508bd-ffdb-47cf-bdfc-e1efe67df071)

 al seleccionar la opcion 1 de el menu de ZONAS, nos lleva a la opcion de Agregar, en donde nos pide cierta informacion 
 para agreara una zona nueva a la base de datos, esta informacion viene esfecificada de el como o con que tipo de dato se quiene que llenar
si los datos dados son correctos, la zona se guardara en la base de datos.


ZONAS __ EDITAR: 
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/f4bfc3f5-43b0-484d-b7e2-81f0e0767f7c)
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/a1e1d4a6-bd07-45d0-95d1-8ff9b21cbd43)

 Al seleccionar la opcion 2 del menu de zonas, nos lleva a editar, donde principalmente, nos pide el id de la zona que
 deseamos eliminar, (Si el id no existe, despues de intentar editar un dato, nos manda una tabla que nos dice que el activo
 no fue encontrado y nos devuelve al menu de zonas), si el id existe, nos deja editar, y nuevamente nos permite agregar la 
 informacion, y guardarla en el servidor.


 ZONAS  __ ELIMINAR:
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/238bb0a5-8278-4c19-8d77-fc81834fd385)

 
 Al seleccionar la opcion 3 del menu de ZONAS, nos lleva a la opcion de eliminar, donde nos pide el id de una zona.
 si el id existe, elimina la zona totalmente de la base de datos.

 
 ZONAS __ BUSCAR
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/71fed349-2e5b-4c8e-85ed-fb89a3339a8a)

 al seleccionar la opcion 4 del Menu de ZONAS, nos lleva a la opcion de buscar, donde nos permite 1. buscar zona por el id 
 2. Buscar zona por el nombre de la zona, 3. buscar zona por la capacidad total,  0. Salir(volver al menu anterior, si esa opcion es seleccionada),
 cada una de estas opciones nos permite buscar dentro de la base de datos la informacion de la zona. 

 
 ZONAS __ REGRESAR AL MENU PRINCIPAL:

al seleccionar la opcion 5, el menu se retrocedera al anterior menu


ASIGNACION DE ACTIVOS:

al seleccionar la opcion 4 de el menu principal Nos lleva a:
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/d52e11ed-d92f-4497-9e23-1cfad40bf296)

ASIGNACION DE ACTIVOS __ CREAR ASIGNACION:
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/3a42ca75-ea84-460a-b62b-e2bfd8575b93)

al seleccionar la opcion 1 de asignacion de activos, nos lleva a la opcion de crear asignacion donde primeramente nos 
que tipo de asignacion es (Persona) o  (Zona), luego nos pregunta el id de la zona o persona a la que se le asignara 
el activo(si el id no existe, muestra mensaje y no sera asignado el activo) y luego el id del encargado del movimiento(Si no existe
el id de el encargado del movimiento no existe, muestra el mensaje pertinente, y no sera asignado el activo), si toda esta informacion 
es correcta, el activo sera asignado correctamente y esta asignacion sera puesta en el historial de activo y en las asignaciones 
de el mismo.


ASIGNACIONES DE ACTIVOS __ BUSCAR ASIGNACION:
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/e2bb6205-eaf4-4fab-9cdc-e139626af6bb)

 al seleccionar la opcion 2 de asignaciones de activos, nos lleva a la opcion de buscar, donde nos permite  buscar las asigaciones del activo por el id, 
  permite introducir el id de el activo que queremos buscar, y nos retorna informacion sobre las asignaciones del activo buscado si es que existe.

 
 ASIGNACIONES DE ACTIVOS __ REGRESAR AL MENU PRINCIPAL:

al seleccionar la opcion 3, el menu se retrocedera al anterior menu



REPORTES:
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/1b64367d-edde-4e76-90e5-dc1f13b9298c)

al seleccionar la opcion 5 de el menu principal Nos lleva a:

REPORTES __  LISTAR TODOS LOS ACTIVOS:

si selecciona la opcion 1: este es un filtro que permite mostrar todos los activos existentes en una lista.

REPORTES __ LISTAR ACTIVOS POR CATEGORIAS:

si selecciona la opcion 2: al seleccionar esta opcion nos lleva al menu: 

que nos permite seleccioanr que tipo de categoria desea listar

REPORTES __ LISTAR ACTIVOS DADOS DE BAJA POR DAÑO:

si selecciona la opcion 3: este es un filtro que permite mostrar en una lista todos los activos que fueron dados de baja por daño

REPORTES __ LISTAR HISTORIAL Y ASIGNACION:

si selecciona la opcion 4: este filtro muestra todos los activos que tienen asignaciones

REPORTES __ LISTAR HISTORIAL DE MOV. DE ACTIVOS:

si selecciona la opcion 5: este filtro pide al usiario el id de el activo que desea mostrar el historial

REPORTES __ REGRESAR AL MENU PRINCIPAL:

si selecciona la opcion 6, se sale al menu principal


MENU MOVIMIENTOS DE ACTIVOS:
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/db1083ed-2a62-429f-9eb2-13d0ce8dacbf)

al seleccionar la opcion 6 de el menu principal Nos lleva a:

MENU MOVIMIENTOS DE ACTIVOS __ RETORNO DE ACTIVOS:
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/5bcaa866-b5f6-4008-9d18-968572a99df2)
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/a797f194-6e10-4d9a-9e8a-aba59b186141)

al seleccionar la opcion 1 de  MENU MOVIMIENTOS DE ACTIVOS, para ret0rnar correctamente el usuario tendra que poner el 
id de el activo que desea retornar existe (si el id deñ actio no existe, se muestra el mensaje y se reinicia) y luego el
usuario da un nro de responsable correcto, el activo fue retornado (poniendole su debido historial).

MENU MOVIMIENTOS DE ACTIVOS __ DAR DE BAJA ACTIVO:
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/7ab7b42a-f500-4e4c-8a3d-3a5c74623c7c)
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/22e757b9-4e9e-4512-a142-15810e872080)

al seleccionar la opcion 2 de  MENU MOVIMIENTOS DE ACTIVOS, para Dar de baja correctamente el usuario tendra que poner el 
id de el activo que desea retornar existe (si el id deñ actio no existe, se muestra el mensaje y se reinicia) y luego el
usuario da un nro de responsable correcto, el activo fue retornado (poniendole su debido historial).



MENU MOVIMIENTOS DE ACTIVOS __ ENVIAR A GARANTIA ACTIVOS
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/1f9bf54e-ac50-4f65-9b88-a9bd0cdbe8d6)

![image](https://github.com/Ineidy/proyectoPython/assets/160775201/66f70418-c13c-4b7b-890e-ea2586ae1e9e)

al seleccionar la opcion 3 de  MENU MOVIMIENTOS DE ACTIVOS, para Dar de baja correctamente el usuario tendra que poner el 
id de el activo que desea retornar existe (si el id deñ actio no existe, se muestra el mensaje y se reinicia) y luego el
usuario da un nro de responsable correcto, el activo fue retornado (poniendole su debido historial).

MENU MOVIMIENTOS DE ACTIVOS __ CAMBIAR ASIGNACION DE ACTIVO
![image](https://github.com/Ineidy/proyectoPython/assets/160775201/490829ec-3bad-42f4-a638-b0d9d9c1448d)

![image](https://github.com/Ineidy/proyectoPython/assets/160775201/a5041b5d-9b63-4cb5-be3f-144b5a44ac51)

al seleccionar la opcion 3 de  MENU MOVIMIENTOS DE ACTIVOS, para Dar de baja correctamente el usuario tendra que poner el 
id de el activo que desea retornar existe (si el id deñ actio no existe, se muestra el mensaje y se reinicia) y luego el
usuario da un nro de responsable correcto, el activo fue retornado (poniendole su debido historial).

