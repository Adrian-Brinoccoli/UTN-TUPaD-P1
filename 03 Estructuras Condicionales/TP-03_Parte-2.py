#6) Ejercicio N°6

import random
from statistics import mode, median, mean

lista_numeros = [random.randint(1, 100) for i in range (100)]

moda = mode(lista_numeros)
mediana = median(lista_numeros)
media = mean(lista_numeros)

print( '\n',moda,'\n' ,mediana,'\n',media,'\n')

#Sesgo posituivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
if media > mediana and mediana > moda:
    print(" Sesgo Positivo ")
    #Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
elif media < mediana and mediana < moda:
    print(" Sesgo negativo ")
    #Sin Sesgo: Cuando la media, la mediana y la moda son iguales.
elif media == mediana and mediana == moda:
    print(" Sin Sesgo ")

else:
    print(" UPPS! Error")

