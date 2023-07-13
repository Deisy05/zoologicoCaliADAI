import main
import time
n = 10

m = 5

k = 2

animales = [
    ("colibri", 1),
    ("mariposa", 3),
    ("alcon", 6),
    ("hipopotamo", 10), 
    ("saltamontes", 2),
    ("loro", 4),
    ("cocodrilo", 7),
    ("tigre", 8), 
    ("leon", 9),
    ("iguana", 5)
    ]

apertura = [["cocodrilo", "tigre", "leon"], ["leon", "hipopotamo", "alcon"], ["mariposa", "colibri", "loro"], ["saltamontes", "iguana", "colibri"], ["tigre", "alcon", "mariposa"], ["hipopotamo", "loro", "cocodrilo"],["leon","cocodrilo","alcon"],["tigre","leon","hipopotamo"]
            ]

partes = [
    [["mariposa", "colibri", "loro"], ["cocodrilo", "tigre", "leon"]],
    [["tigre", "alcon", "mariposa"], ["saltamontes", "iguana", "colibri"]],
    [["hipopotamo", "loro", "cocodrilo"], ["leon", "hipopotamo", "alcon"]],
    [["leon","cocodrilo","alcon"],["tigre","leon","hipopotamo"]] 
    ]

print("total escenas: ", ((m-1)*k)*2 )
#Llamar mi función
inicioTiempo=time.time()*1000
#main.espectaculo(n, m, k, animales, apertura, partes,'insertion_sort')
main.espectaculo(n, m, k, animales, apertura, partes,'any_sort')
#main.espectaculo(n, m, k, animales, apertura, partes,'another_sort')
finalTiempo=time.time()*1000
print('TIEMPO DEL ALGORITMO: ', (finalTiempo-inicioTiempo))