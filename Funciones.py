def Crearcarrera (carreras):
     print("Ingrese carrera")
     nombre = input("Nombre : ")
     dicCarrera = {"carrera":nombre,"clase":[]}
     carreras.append(dicCarrera)
     print("carrera creada ")
     
def Leercarrera (carreras):
    print("Leer (mostrar) carreras")
    for carrera in carreras:
     print("- Nombre :" + carrera["carrera"])
 
def actualizarcarrera (carreras):
 carreraactualizar = input("Ingrese el nombre de la carrera")
 nuevonombre=input("Ingrese el nuevo nombre de la carrera")
 for carrera in carreras:
    if carrera["carrera"] == carreraactualizar:
        carrera["carrera"] = nuevonombre
        print("Carrera actualizada")
        
def borrarcarrera (carreras):
    carreraborrar=input("Ingrese el nombre de la carrera")
    encontrada = False
    for carrera in carreras :
     if carrera["carrera"]== carreraborrar:
         carreras.remove(carrera)
         encontrada=True
         print("Carrera eliminada")
         break
     if not encontrada:
         print("no existe")
         
def MENU():
    carreras=[]
    seguir = True
    
    while seguir:
        print(carreras)
        print(carreras)
        print("++++++++++++++++ Menu ++++++++++++++++++")
        print("1. Crear carrera")
        print("2. Leer carrera")
        print("3. Actualizar carrera")
        print("4. Borrar carrera")
        print("5. Salir")
        opcion = int(input("Ingrese su opcion: "))
        print("----------------------------------")
        
    if opcion==1:
        Crearcarrera(carreras)
    elif opcion==2:
        Leercarrera(carreras)
    elif opcion==3:
        actualizarcarrera(carreras)
    elif opcion==4:
        borrarcarrera(carreras)
    elif opcion==5:
        print("Hasta la proxima")
        seguir=False