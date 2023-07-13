#ordenar escenas de aacuerdo a grandeza de cada una
def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and ((A[j][0] == key[0] and max(A[j][1]) > max(key[1])) or A[j][0] > key[0] ):
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    
   
#ordenar elementos de la escena
def insertion_sort_scene(arreglo):
    for sum, B in arreglo:
        for i in range(1, len(B)):
            valor = B[i]
            j = i - 1
            while j >= 0 and B[j] > valor:
                B[j + 1] = B[j]
                j -= 1
            B[j + 1] = valor


#ordenar escenas de aacuerdo a grandeza de cada una
# def any_sort(A):
#     # Encontrar el valor máximo en la lista para determinar el tamaño del arreglo de conteo
#     max_value = max(A, key=lambda x: x[0])[0]

#     # Crear el arreglo de conteo
#     count = [0] * (max_value + 1)

#     # Contar la frecuencia de cada elemento en la lista de entrada
#     for tup in A:
#         count[tup[0]] += 1

#     # Modificar la lista original A para que contenga los elementos ordenados
#     index = 0
#     for i in range(len(count)):
#         for j in range(count[i]):
#             A[index] = (i, A[index][1])
#             index += 1

def any_sort(arr):
    # Encontrar el valor máximo en la lista
    max_value = max(arr, key=lambda x: x[0])

    # Crear una lista de conteo con el tamaño del valor máximo más uno
    count = [0] * (max_value[0] + 1)

    # Contar la frecuencia de cada elemento en la lista de entrada
    for num in arr:
        count[num[0]] += 1

    # Actualizar la lista de conteo para almacenar la posición final de cada valor
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Construir una lista ordenada en la lista de entrada
    sorted_arr = [None] * len(arr)
    for num in arr:
        count[num[0]] -= 1
        sorted_arr[count[num[0]]] = num

    # Actualizar la lista original con la lista ordenada
    arr[:] = sorted_arr[:]



            


    
#ordenar elementos de la escena
def any_sort_scene(B):
    for i in range(len(B)):
        sum, arr = B[i]
        new_arr = counting_sort(arr)
        B[i] = (sum, new_arr)


def counting_sort(arr):
    # Determinar el rango de valores posibles en el arreglo
    min_value = min(arr)
    max_value = max(arr)
    range_values = max_value - min_value + 1
    
    # Crear un arreglo de contadores y inicializarlo en cero
    count = [0] * range_values
    
    # Contar la frecuencia de cada valor en el arreglo original
    for num in arr:
        count[num - min_value] += 1
    
    # Calcular las posiciones finales de los elementos
    for i in range(1, range_values):
        count[i] += count[i - 1]
    
    # Crear un arreglo auxiliar
    result = [0] * len(arr)
    
    # Recorrer el arreglo original en orden inverso
    for num in reversed(arr):
        position = count[num - min_value] - 1
        result[position] = num
        count[num - min_value] -= 1
    
    return result



def another_sort(A):
    new=merge(left, right)
    if len(A) <= 1:
        return A

    mid = len(A) // 2
    left = another_sort(A[:mid])
    right = another_sort(A[mid:])
    # Actualizar la lista original con la lista ordenada
    A[:] = new[:]


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0] or (left[i][0] == right[j][0] and max(left[i][1]) < max(right[j][1])):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

    

#def another_sort_scene(B): 
# ejemp= [(15, [1, 5, 9]), (15, [5, 1, 4])]

# another_sort(ejemp)
# print("ordenar escena   ", ejemp)