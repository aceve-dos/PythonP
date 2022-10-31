#Python tiene varios tipos de datos compuestos, utilizados para agrupar otros valores. El más versátil es la lista, la cual puede ser escrita como una lista de valores separados por coma (ítems) entre corchetes. Las listas pueden contener ítems de diferentes tipos, pero usualmente los ítems son del mismo tipo.

cuadrados = [1, 4, 9, 16, 25]
print(cuadrados)

#Al igual que las cadenas (y todas las demás tipos integrados sequence), las listas se pueden indexar y segmentar:
cuadrados = [1, 4, 9 , 16, 25]
print(cuadrados[0])
print(cuadrados[-1])
print(cuadrados[-3:])

#Todas las operaciones de rebanado retornan una nueva lista que contiene los elementos pedidos. Esto significa que la siguiente rebanada retorna una shallow copy de la lista:
print(cuadrados[:]) 

#Las listas también admiten operaciones como concatenación:
print(cuadrados + [36, 49, 64, 81, 100])

#A diferencia de las cadenas, que son immutable, las listas son de tipo mutable, es decir, es posible cambiar su contenido:
cubos = [1, 8, 27, 65, 125]
cubo = 4 ** 3
print(cubo)
cubos [3] = 64
print (cubos)

#También puede agregar nuevos elementos al final de la lista, utilizando el método append() (vamos a ver más sobre los métodos luego):
cubos.append(216)
cubos.append(7 ** 3)
print(cubos)

#También es posible asignar a una rebanada, y esto incluso puede cambiar la longitud de la lista o vaciarla totalmente:
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letras)
#reemplaza algunos valores
letras[2:5] = ['C', 'D', 'E']
print(letras)
#ahora se borran
letras[2:5] = []
print(letras)
#limpia toda la lista y reemplaza todos los elementos con una lista limpia
letras[:] = []
print(letras)

#La función predefinida len() también sirve para las listas
letras = ['a', 'b', 'c', 'd']
print(len(letras))

#Es posible anidar listas (crear listas que contengan otras listas), por ejemplo:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])