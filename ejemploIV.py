import main
import time
n = 9

m = 6

k = 3

animales = [
    ("mariposa", 1),
    ("alcon", 2),
    ("hipopotamo", 9),
    ("cocodrilo", 5),
    ("tigre", 6), 
    ("leon", 8),
    ("panteranegra", 7),
    ("cebra", 3),
    ("boa", 4)

]

apertura= [["alcon", "mariposa", "hipopotamo"], ["alcon", "leon", "boa"], ["tigre", "cocodrilo", "leon"], ["panteranegra", "cebra", "boa"], ["mariposa", "cocodrilo", "boa"], ["mariposa", "tigre", "leon"], ["hipopotamo", "cocodrilo", "panteranegra"], ["alcon", "cebra", "boa"], ["alcon", "hipopotamo", "cebra"], ["tigre", "leon", "panteranegra"], ["tigre", "cocodrilo", "cebra"], ["alcon", "mariposa", "panteranegra"],["alcon", "tigre", "panteranegra"], ["hipopotamo", "cocodrilo", "cebra"], ["hipopotamo", "leon", "boa"]
]
    


partes=[
    [["alcon", "mariposa", "hipopotamo"], ["tigre", "cocodrilo", "leon"], ["panteranegra", "cebra", "boa"]],[["mariposa", "tigre", "leon"], ["hipopotamo", "cocodrilo", "panteranegra"], ["alcon", "cebra", "boa"]],[["alcon", "hipopotamo", "cebra"], ["mariposa", "cocodrilo", "boa"], ["tigre", "leon", "panteranegra"]],[["tigre", "cocodrilo", "cebra"], ["hipopotamo", "leon", "boa"], ["alcon", "mariposa", "panteranegra"]],[["alcon", "tigre", "panteranegra"], ["hipopotamo", "cocodrilo", "cebra"], ["alcon", "leon", "boa"]]
]

print("total escenas: ", ((m-1)*k)*2 )
#Llamar mi función
inicioTiempo=time.time()*1000
#main.espectaculo(n, m, k, animales, apertura, partes,'insertion_sort')
main.espectaculo(n, m, k, animales, apertura, partes,'any_sort')
#main.espectaculo(n, m, k, animales, apertura, partes,'another_sort')
finalTiempo=time.time()*1000
print('TIEMPO DEL ALGORITMO: ', (finalTiempo-inicioTiempo))