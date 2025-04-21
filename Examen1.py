# UNAM
# Faculta de Ingenieria 
# Sitemas Operativos 
# Examen 1
# Profesor Ing. Cruz Sergio Aguilar Díaz 
# Semestre 2024-1
#Sanchez Mayen Tristan Qesen

import math

def memDim( mem ): #funcion que simula la gestion de memoria dinamica
    
    menusec = 0 #inicia la variable en 0
    proc = int(input("Ingrese el tamaño del proceso: ")) #almacena el valor en la variable proc como numero entero
    mem -= proc #resta el tamaño del proceso a la variable mem
    
    while menusec != 2: #incia un bucle que se ejecutara mientras menusec no sea igual a 2
        
        print("\nMemoria disponible: {}kb\n".format(mem)) #imprime la cantidad de memoria disponible
        menusec = int(input("¿Desea agregar otro proceso?\n1) Si\n2) No\n->" )) #almacena su respuesta en menusec como un numero entero
        if menusec == 1: #si el usuario eligio otro proceso se ejecuta el if
            proc = int(input("Ingrese el tamaño del proceso: "))
            mem -= proc
            if mem == 0 or mem < 0: #comprueba si la memoria disponible es igual a 0, si es menor no hay memoria disponible
                print("Memoria Insuficiente") 
        elif menusec == 2: #si el usuario no agrega otro proceso se termina el bucle
            break
        else:
            print("Ingrese una opcion valida")
    return mem #devuelve la cantidad de memoria disponible despues de realizar el bucle

def part( mem ):  #funcion que simula el particionamiento de memoria
    numero = int(input("Ingresa el número de particiones requeridas: ")) #almacena el valor como numero entero
    lista = [] #incia una lista que almacena los tamaños de las particiones

    for i in range(numero): #se ejecutara numero veces donde i sera un valor desde 0 hasta numero -1
        elemento = int(input("Ingresa el tamaño de la particion {} -> ".format(i+1))) #almacena el valor en elemento como numero entero
        lista.append(elemento) #agrega el tamaño de la particion a la lista

    while True: #inicia un bucle infinito para permitir realizar varias operaciones
        print("\n----- Particiones -----")
        print("1) Mostrar lista")
        print("2) Editar particion")
        print("3) Agregar particion")
        print("4) Calcular espacio")
        print("5) Salir")

        opcion = int(input("Ingrese una opción: ")) #solicita que el usuario ingrese una opcion en el menu y lo almacena como numero entero

        if opcion == 1: #comprueba si elegio la opcion mostrar lista  y la muestra
            print("Particiones: {}".format(lista))

        elif opcion == 2: #comprueba si elegio la opcion editar particion
            indice = int(input("Ingresa el índice de la particion a editar: ")) #solicita al usuario que ingrese el indice de la particion y almacena el valor como numero entero
            if 0 <= indice < len(lista): #comprueba si el indice esta dentro de los limites validos de la lista de particiones
                nuevo_elemento = int(input("Ingresa el nuevo tamaño: ")) 
                lista[indice] = nuevo_elemento #actualiza el tamaño de la particion en la lista con el nuevo valor ingresado
                print("Particion editada correctamente.")
            else:  
                print("Índice inválido.")

        elif opcion == 3: #comprueba si eligio la opcion agregar particion
            if sum(lista) == mem: #comprueba si la suma de todos los tamaños de las particiones es igual a la memoria total disponible
                print("No se pueden crear mas particiones, memoria insuficiente\n")
            else: #si todavia hay memoria disponible, solicita al usuario que ingrese el tamaño de la nueva particion
                nuevo_elemento = int(input("Ingrese el nuevo elemento: "))
                lista.append(nuevo_elemento)
                print("Particion agregada correctamente")

        elif opcion == 4: #comprueba si el usuario eligio calcular espacio
            suma = sum(lista) #calcula la suma de todos los tamaños de las particiones en la lista 
            print("Las particiones son {} y juntas forman {} kb\n".format(lista, suma)) #imprime la lista de las particiones y la suma de sus tamaños

        elif opcion == 5: #comprueba si el usuario eligio salir 
            print("¡Hasta luego!")
            break
        
        else:
            print("Ingresa una opcion valida")
        return mem #devuelve la cantidad de memoria disponible despues de que el usuario haya terminado de realizar las operaciones

def seg( mem ): #funcion que simula la segmentacion de memoria
    
    proc = int(input("Ingresa un tamaño de proceso -> ")) 
    while mem > proc or mem == proc: #inicia un bucle que se ejecuta mientras que la memoria disponible sea mayor que el tamaño del proceso o igual a el
        segm = math.floor(proc/3) #calcula el tamaño de cada segmento al dividir el tamaño de proceso en 3 partes iguales
        #imprime la informacion sobre la segmentacion en 3 partes
        print("Segmentación en 3 partes")
        print("     Data Segment -> {}kb".format(segm))
        print("     Code Segment -> {}kb".format(segm))
        print("     Stack Segment -> {}kb".format(segm))
        print("     Memoria para procesos -> {}kb".format(segm))
    else: 
        print("Memoria Insuficiente")
        
    return mem #devuelve la cantidad de memoria dispobible de que el usuario haya terminado de realizar operaciones

def main(): #funcion que representa la parte principal del programa
    menu = 0
    memoria = 2048 #cantidad total de memoria disponible
 
    #imprime el encabezado con nuestros datos
    print("""            
            Examen 1 Sistemas Operativos
            Grupo 01 
            Manejo de Memoria
            Pivaliu SO de {} kb
                """.format(memoria))
     
    while menu != 5: #inicia un bucle que se ejecuta mientras que menu no sea igual a 5 (el usuario no ha elegido salir)
        
        #imprime el menu de opciones a elegir
        print("""   Elija una opción:
                    
                1)  Memoria Estática
                2)  Memoria Dinámica
                3)  Particionamiento de memoria
                4)  Segmentacion de memoria
                5)  Salir
                    """)
        
        menu = int(input()) #solicita al usuario ingresar una opcion y la guarda como numero entero
        
        if menu == 1: #comprueba si el usuario elegio memoria estatica e imprime su informacion
            print("Memoria estatica de tamanio {} kb\n".format(memoria))
        elif menu == 2: #comprueba si el usuario elegio memoria dinamica e imprime su informacion
            memoria = memDim(memoria)
        elif menu == 3: #comprueba si el usuario elegio particionamiento de memoria e imprime su informacion
            memoria = part(memoria)
        elif menu == 4: #comprueba si el usuario elegio segmentacion de memoria e imprime su informacion
            memoria = seg(memoria)
        elif menu == 5: #comprueba si el usuario elegio salir e imprime su informacion
            print("Hasta luego! :D")
            break
        else: 
            print("Ingrese una opcion valida")
main() #llama a la funcion main para ejecutar el programa