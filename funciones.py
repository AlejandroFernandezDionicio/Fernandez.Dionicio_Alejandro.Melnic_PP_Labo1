import json
def opcion_menu():
    '''Parametros: Ninguno'''
    '''Descripcion: Muestra por terminal las opciones y pide el usuario elegir 1'''
    '''Retorno: Ninguno '''
    print("1-Cargar archivo\n2-Imprimir lista\n3-Asignar totales\n4-Filtrar por tipo\n5-Mostrar servicios\n6-Guardar servicios\n7-Salir")
    opcion = str(input("Opcion: "))
    return opcion

def mostrar_titulo():
    '''Muestra por pantalla los datos'''
    print(f"{"ID_SERVICIO":<23} {"DESCRIPCION":<23} {"TIPO":<23} {"PRECIO_UNITARIO":<23} {"CANTIDAD":<23} {"TOTAL_SERVICIO":<23}")

def cargar_elementos(nombre_archivo:str):
    '''Recibe como parametro la ubicaciond el archivo
       abre el archivo
       retorna los datos dentro del archivo'''
    try:
        with open(nombre_archivo, "r") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        print(f"Archivo no encontrado: {nombre_archivo}")
        return False
    
def mostrar_datos(lista:list):
    '''Recibe como parametro una lista
       recorre la lista para mostrar los value de las keys'''
    mostrar_titulo()
    for elemento in lista:
        print(f"{elemento["id_servicio"]:<23} {elemento["descripcion"]:<23} {elemento["tipo"]:<23} {elemento["precioUnitario"]:<23} {elemento["cantidad"]:<23} {elemento["totalServicio"]:<23}")

def calcular_total(lista:list):
    '''Recibe como parametro una lista
       Recorre la lista y en una variable guarda las value de las key asignadas y los castea a float
       con un lambda hace un calculo para tener el total y este mismo se agrega como valor nuevo a la key totalservicio'''
    for elemento in lista:
        cantidad = float(elemento["cantidad"])
        precio = float(elemento["precioUnitario"])
        total = (lambda cantidad,precio: cantidad * precio)(cantidad,precio)
        elemento["totalServicio"] = total

def pedir_datos():
    '''No recibe parametros
       pide al usuario una clave en este caso ya declaradas en la variable lista_datos
       donde si el usuario elige una de estas la funcion lo retorna
       sino repite la pregunta'''
    while True:
        lista_keys = ["id_servicio","descripcion","tipo","precioUnitario","cantidad","totalServicio"]
        key = input("Ingrese la key que quiera tener el archivo nuevo : ")
        if key in lista_keys:
            return key
        else:
            print(f"Error, intende de nuevo")

def generar_archivo(nombre_archivo:str,key:str,lista:list):
    '''Recibe como parametro la ubicacion del archivo una key y una lista
       abre el archivo en modo de w+ primero escribe el titulo que sera la key
       y recorre la lista para escribir las value de la key en el nuevo archivo generado'''
    try:
        with open(nombre_archivo, "w+") as archivo:
            archivo.write(f"{key}\n")
            for elemento in lista:
                linea = f"{elemento[key]}\n"
                archivo.write(linea)
            
    except FileNotFoundError:
        print(f"Archivo no encontrado: {nombre_archivo}")
        return False

def pedir_nombre():
    nombre = input("Ingrese el nombre que tendra el nuevo archivo")
    return nombre + ".json"

def ordenamiento(lista:list,clave:str):
    '''Recibe como parametros, una lista y una cadena
       con el metodo sorted y un lambda que me devuelve el contenido de una key
       retorna esta misma como una lista ordenada'''
    lista_ordenada = sorted(lista, key=lambda elemento: elemento[clave])
    return lista_ordenada

def guardar_json(nombre_archivo:str,lista:list): 
    '''Recibe como parametro una ubicacion de archivo, y una lista
       Abre el archivo en modo escritura y lectura recorre la lista y escribe los elementos
       en un nuevo archivo'''
    try:
        with open(nombre_archivo, "w+") as archivo:
            for elemento in lista:
                linea = f"{elemento}\n"
                archivo.write(linea)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {nombre_archivo}")
        return False

