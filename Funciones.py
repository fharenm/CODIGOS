carreras=[]
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
 carreraActualizar = input("Ingrese nombre de la carrera : ")
 print("1.ACTUALIZAR NOMBRE DE LA CARRERA ")
 print("2.AGREGAR CLASE  DE LA CARRERA")
 print("3.ELIMINAR CLASE DE LA CARRERA")
 print("4.ACTUALIZAR CLASE DE LA CARRERA")
 print("----------------------------------")
 opcion2 = int(input("ingrese su opcion :"))
 if opcion2==1:
         nuevoValor = input("Ingrese nuevo nombre de la carrera : ")
         for carrera in carreras:
             if carrera["carrera"] == carreraActualizar:
                 carrera["carrera"] = nuevoValor
                 print("carrera actualizada ")
                 print("----------------------------------")
 elif opcion2==2:  
         nombreclase=input("Ingrese la clase para la carrera : ")
         for carrera in carreras:
           if "clase" not in carrera:
             carrera["clase"]=[nombreclase]
           else:
             carrera["clase"].append(nombreclase)
             print("se agrego la clase correctamente ")
             print("----------------------------------")
 elif opcion2==3:
            borrarclase=input("Ingrese la clase que desea borrar :")
            for carrera in carreras:
                if carrera["carrera"] == carreraActualizar and "clase" in carrera:
                    if borrarclase in carrera["clase"] :
                     carrera["clase"].remove(borrarclase)
                     print("la clase se elimino")
                     print("----------------------------------")
 elif opcion2==4:
            actualizarclase=input("Ingrese la clase que desea actualizar")
            nombrenuevoclase=input("Ingrese el nuevo nombre de la clase ")
            for carrera in carreras:
                if carrera["carrera"] == carreraActualizar and "clase" in carrera:
                    if actualizarclase in carrera["clase"]:
                     carrera["clase"]=[nombrenuevoclase]
                     
                
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
        