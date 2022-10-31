#Además de la sentencia while que acabamos de introducir, Python soporta las sentencias de control de flujo que podemos encontrar en otros lenguajes, con algunos cambios.

#Sentencia if
from collections import UserString


x = int(input("Ingresa un entero: "))

if x < 0:
    x = 0
    print("El negativo cambió a 0")
elif x == 0:
    print("Cero")
elif x == 1:
    print("Simple 1")
else:
    print("Más")


#Puede haber cero o más bloques elif, y el bloque else es opcional. La palabra reservada “elif’es una abreviación de “else if”, y es útil para evitar un sangrado excesivo. Una secuencia if … elif … elif … sustituye las sentencias switch o case encontradas en otros lenguajes.

#Si necesitas comparar un mismo valor con muchas constantes, o comprobar que tenga un tipo o atributos específicos puede que encuentres útil la sentencia keyword:!match. Para más detalles véase La sentencia match.

#For

#La sentencia for en Python difiere un poco de lo que uno puede estar acostumbrado en lenguajes como C o Pascal. En lugar de siempre iterar sobre una progresión aritmética de números (como en Pascal) o darle al usuario la posibilidad de definir tanto el paso de la iteración como la condición de fin (como en C), la sentencia for de Python itera sobre los ítems de cualquier secuencia (una lista o una cadena de texto), en el orden que aparecen en la secuencia. Por ejemplo:

palabras = ['gato', 'ventana', 'defenestrar']

for w in palabras:
    print(w, len(w))

#Código que modifica una colección mientras se itera sobre la misma colección puede ser complejo de hacer bien. Sin embargo, suele ser más directo iterar sobre una copia de la colección o crear una nueva colección:

#creando una colección de palabras
usuarios = {'Hans': 'activo', 'Eleonor' : 'inactivo', 'Carlos' : 'activo'}

#Iterar sobre una copia
for user, status in usuarios.copy().items():
    if status == 'inactivo':
        del usuarios[user]

#Creando una nueva coleccion
usuarios_activos = {}
for user, status in usuarios.items():
    if status == 'activo':
        usuarios_activos[user] = status


#Range

#Si se necesita iterar sobre una secuencia de números, es apropiado utilizar la función integrada range(), la cual genera progresiones aritméticas:

for i in range(5):
    print(i)





