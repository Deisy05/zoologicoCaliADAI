import opciones

def espectaculo(n, m, k, animales, apertura, partes, miAlgoritmo):
    
    #validarlas entradas                                                               
    escenas_esperadas = k * (m - 1)                                                 

    if escenas_esperadas != len(apertura):                                          
        if len(apertura) < escenas_esperadas:                                       
            print(f"El número de escenas es menor que {escenas_esperadas}.")        
            print(f"Necesitas {escenas_esperadas - len(apertura)} escena más.")     
        else:
            print(f"Número de escenas excede a {escenas_esperadas}.")               
            print(f"Tienes {len(apertura) - escenas_esperadas} escena extra.")
        return

    def combinaLista(lista):
        resultado = []
        for sublistas in lista:
            for elemento in sublistas:
                resultado.append(elemento)
        return resultado

    partes_combinadas = combinaLista(partes)

    def validarEntradas(lista1, lista2):
        if len(lista1) != len(lista2):
            return False

        elementos_lista2 = list(lista2)

        for elemento in lista1:
            if elemento in elementos_lista2:
                elementos_lista2.remove(elemento)
            else:
                return False

        return len(elementos_lista2) == 0

    if not validarEntradas(apertura, partes_combinadas):
        print("Las listas no son compatibles. Verificarlas nuevamente")
        exit()


    # pasar animales de apertura a numeros
    transformarArreglo(apertura, animales, 'animal')
    # pasar animales del arreglo partes a numeros
    for parte in partes:
        transformarArreglo(parte, animales, 'animal')

    #determinar algoritmos a usar
    if(miAlgoritmo=='insertion_sort'):
        sort=opciones.insertion_sort
        sort_scene=opciones.insertion_sort_scene
    elif (miAlgoritmo=='any_sort'):
        sort=opciones.any_sort
        sort_scene=opciones.any_sort_scene
    
    # Ordenar apertura de acuerdo a la suma de grandezas de cada escena, y ordenar elementos de cada escena
    sumasDeEscenas = sumaEscena(apertura)
    combinar = list(zip(sumasDeEscenas, apertura))
    sort(combinar)

    # ordenar elementos de las escenas
    sort_scene(combinar)

    # Ordenar escenas de cada parte de acuerdo a la suma de grandezas y ordenar elementos de cada escena
    partesOrdenas = []
    for parteA in partes:
        sumas = sumaEscena(parteA)
        combinacion = list(zip(sumas, parteA))
        sort(combinacion)
        partesOrdenas.append(combinacion)
        sort_scene(combinacion)

    # ordenar listado de partes de acuerdo a sumas totales
    def suma(lista):
        total = 0
        for numero in lista:
            total += numero
        return total

    resultado = [suma(tupla[0] for tupla in elemento) for elemento in partesOrdenas]
    combinadosGrandeza_Partes = list(zip(resultado, partesOrdenas))
    sort(combinadosGrandeza_Partes)

    #Obtener lista de escenas
    def obtener_lista_de_escenas(lista):
        segundos_elementos = []
        for tupla in lista:
            segundo_elemento = tupla[1]
            segundos_elementos.append(segundo_elemento)
        return segundos_elementos

    listaDeEscenas = obtener_lista_de_escenas(combinar)

    #Obtener lista de partes
    def listar_listas_anidadas(tuplas):
        listas_anidadas = []
        for tupla in tuplas:
            for sublist in tupla[1]:
                listas_anidadas.append(sublist[1])
        return listas_anidadas

    listaDePartes = listar_listas_anidadas(combinadosGrandeza_Partes)

    #pasar datos a animales
    transformarArreglo(listaDeEscenas,animales,'numero')
    transformarArreglo(listaDePartes,animales,'numero')

    print('El orden en el que se debe presentar el espectaculo es:\nApertura: ',listaDeEscenas)

    #Estructurar partes
    def estructurarPartes(k, lista):
        partes = []
        for i in range(0, len(lista), k):
            parte = lista[i:i + k]
            partes.append(parte)
        return partes

    partesEstructuradas = estructurarPartes(k, listaDePartes)
    for i, parte in enumerate(partesEstructuradas):
        print(f"parte{i + 1}: {parte}")

    #Hallar maxima y minima participacion
    def contandoMisAnimales(animales):
        contador = {}
        for lista in animales:
            for animal in lista:
                if animal in contador:
                    contador[animal] += 1
                else:
                    contador[animal] = 1

        max_repeticiones = float('-inf')
        min_repeticiones = float('inf')

        for repeticiones in contador.values():
            if repeticiones > max_repeticiones:
                max_repeticiones = repeticiones
            if repeticiones < min_repeticiones:
                min_repeticiones = repeticiones

        animales_mas_repetidos = [animal for animal, repeticiones in contador.items() if
                                  repeticiones == max_repeticiones]
        animales_menos_repetidos = [animal for animal, repeticiones in contador.items() if
                                    repeticiones == min_repeticiones]

        return animales_mas_repetidos, max_repeticiones * 2, animales_menos_repetidos, min_repeticiones * 2

    animales_mas_repetidos, repeticiones_max, animal_menos_repetido, repeticiones_min = contandoMisAnimales(listaDeEscenas)

    print("Los animales que más participaron:", animales_mas_repetidos, "en", repeticiones_max, "escenas")
    print("Los animales que menos participaron:", animal_menos_repetido, "en", repeticiones_min, "escenas")

    #Escenas de mayor y menor grandeza
    escenaMenorGrandeza = combinar[0][1]
    escenaMayorGrandeza = combinar[-1][1]
    print("la escena de Menor Grandeza", escenaMenorGrandeza)
    print("la escena de Mayor Grandeza", escenaMayorGrandeza)

    #promedio de grandeza
    def promedio(lista):
        suma = 0
        for num in lista:
            suma += num
        promedio = suma / len(lista)
        return promedio

    promedio = round(promedio(sumasDeEscenas),2)
    print("promedio de grandeza del espectáculo:", promedio)

    return


# sumas de cada escena
def sumaEscena(A):
    totalSumas = []
    for escena in A:
        totalSumas.append(sum(escena))
    return totalSumas

# Pasar el arreglo de animales a numeros o viceversa
def transformarArreglo(A, animales, opcion):
    for i in range(len(A)):
        for j in range(len(A[i])):
            elemento = A[i][j]
            for animal in animales:
                if opcion == 'animal' and animal[0] == elemento:
                    A[i][j] = animal[1]
                    break
                elif opcion == 'numero' and animal[1] == elemento:
                    A[i][j] = animal[0]
                    break


