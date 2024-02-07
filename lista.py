# crear 
#leer
#actualizar
#borrar

#crear las carreras
#crear las clases
carreras = []
seguir = True

while seguir:
    print(carreras)
    print("++++++++++++++++ Menu ++++++++++++++++++")
    print("1. Crear carrera")
    print("2. Leer carrera")
    print("3. Actualizar carrera")
    print("4. Borrar carrera")
    print("5. Salir")
    opcion = int(input("Ingrese su opcion: "))

    print("----------------------------------")
    if opcion == 1:
        print("Ingresar carrera")
        nombre = input("Nombre : ")
        dicCarrera = {}
        dicCarrera["carrera"] = nombre
        carreras.append(dicCarrera)
    elif opcion == 2:
        print("Leer (mostrar) carreras")
        for carrera in carreras:
         print("- Nombre :" + carrera["carrera"])
         print("-----------------------------------")
    elif opcion == 3:
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
                    else:
                     carrera["clase"].append(nombrenuevoclase)
                    print("se actualizo la clase correctamente ")
                    print("----------------------------------")
    elif opcion == 4:
        carreraBorrar = input("Ingrese nombre de la carrera : ")
        indice = 0
        encontrado = False
        for carrera in carreras:
            if carrera["carrera"] == carreraBorrar:
                encontrado = True
                break
            else :
                indice = indice + 1

        if encontrado :
            carreras.remove(carreras[indice])
            print("Elemento borrado")
        else:
            print("No existe")
    elif opcion == 5:
        print("Hasta la proxima")
        seguir = False
    print("----------------------------------")

"""
[0  {'carrera': 'IS'},
 1  {'carrera': 'CIVIL'},
 2  {'carrera': 'IND'}]

"""
