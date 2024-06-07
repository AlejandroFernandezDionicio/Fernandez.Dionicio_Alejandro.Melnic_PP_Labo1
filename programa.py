from funciones import*
bandera_menu_opcion_1 = False
bandera_menu_opcion_5 = False
while True:
    opcion = opcion_menu()
    if opcion == "1":
       bandera_menu = True
       lista = cargar_elementos("data.json")
       print("DATOS CARGADOS")
    elif opcion == "2":
        if bandera_menu == True:
            mostrar_datos(lista)
        else:
            print("PRIMERO INGRESE A LA OPCION 1")
    elif opcion == "3":
        if bandera_menu == True:
            calcular_total(lista)
            print("TOTAL CALCULADO A CADA SERVICIO")
        else:
            print("PRIMERO INGRESE A LA OPCION 1")
    elif opcion == "4":
        if bandera_menu == True:
            nombre = pedir_nombre()
            key = pedir_datos()
            generar_archivo(nombre,key,lista)
        else:
            print("PRIMERO INGRESE A LA OPCION 1")
    elif opcion == "5":
        if bandera_menu == True:
            bandera_menu_opcion_5 = True
            lista_ordenada = ordenamiento(lista,"descripcion")
        else:
            print("PRIMERO INGRSE A LA OPCION 1")
    elif opcion == "6":
        if bandera_menu_opcion_1 == True and bandera_menu_opcion_5 == True:
            guardar_json(lista_ordenada)
        else:
            print("PRIMERO INGRESE A LA OPCION 1 O OPCIONES 5")
    elif opcion == "7":
        break