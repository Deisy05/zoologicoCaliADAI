import main
import time

n = 6

m = 3

k = 2

animales = [
    ("ciempies", 1),
    ("libelula", 2),
    ("gato", 3),
    ("perro", 4),
    ("tapir", 5),
    ("nutria", 6)
]

apertura = [["tapir", "nutria", "perro"], ["tapir", "perro", "gato"], ["ciempies", "tapir", "gato"],
            ["gato", "ciempies", "libelula"]]

partes = [[["tapir", "nutria", "perro"], ["ciempies", "tapir", "gato"]],
          [["gato", "ciempies", "libelula"], ["tapir", "perro", "gato"]]
          ]


print("total escenas: ", ((m-1)*k)*2 )
#Llamar mi función
inicioTiempo=time.time()*1000
#main.espectaculo(n, m, k, animales, apertura, partes,'insertion_sort')
main.espectaculo(n, m, k, animales, apertura, partes,'any_sort')
#main.espectaculo(n, m, k, animales, apertura, partes,'another_sort')
finalTiempo=time.time()*1000
print('TIEMPO DEL ALGORITMO: ', (finalTiempo-inicioTiempo))