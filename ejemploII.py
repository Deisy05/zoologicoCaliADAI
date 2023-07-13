import main
import time
n = 9

m = 4

k = 3

animales = [
    ("leon", 9),
    ("panteranegra", 7),
    ("cebra", 6),
    ("cocodrilo", 5), 
    ("boa", 4),
    ("loro", 2),
    ("caiman", 3),
    ("tigre",8), 
    ("capibara", 1)
    ]

grandezas = [9, 7, 6, 5, 4, 2, 3, 8, 1]

apertura = [["caiman", "capibara", "loro"], ["boa", "caiman", "capibara"], ["cocodrilo", "capibara", "loro"], ["panteranegra", "cocodrilo", "loro"], ["tigre", "loro", "capibara"], ["leon", "caiman", "loro"], ["leon", "cocodrilo", "boa"], ["leon", "panteranegra", "cebra"], ["tigre", "cebra", "panteranegra"]]

partes = [
    [['caiman', 'capibara', 'loro'], ['tigre', 'loro', 'capibara'], ['tigre', 'cebra', 'panteranegra']],
    [['panteranegra', 'cocodrilo', 'loro'], ['leon', 'panteranegra', 'cebra'], ['cocodrilo', 'capibara', 'loro']],
    [['boa', 'caiman', 'capibara'], ['leon', 'caiman', 'loro'], ['leon', 'cocodrilo', 'boa']] 
    ]


print("total escenas: ", ((m-1)*k)*2 )
#Llamar mi función
inicioTiempo=time.time()*1000
#main.espectaculo(n, m, k, animales, apertura, partes,'insertion_sort')
main.espectaculo(n, m, k, animales, apertura, partes,'any_sort')
#main.espectaculo(n, m, k, animales, apertura, partes,'another_sort')
finalTiempo=time.time()*1000
print('TIEMPO DEL ALGORITMO: ', (finalTiempo-inicioTiempo))