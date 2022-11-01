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


#range

print(list(range(5,10)))
print(list(range(0,10,3)))
print(list(range(-10, -100, -30)))

#iteraciones de una secuencia
a = ['Mary', 'had', 'a', 'pequeña', 'lamb']
for i in range (len(a)):
    print(i, a[i])

#enumerate y range

print(range(10))

#sum
print(sum(range(4)))

#break continue y else: buscador de números primos.

for n in range(2,10):
    for x in range (2,n):
        if n % x == 0:
            print(n, 'squals', x, '*', n // x)
            break
    else:
        print(n, 'es un número primo')

#continue hace la continuación del ciclo.

for num in range(2,10):
    if num % 2 == 0:
        print("Buscando un even número", num)
        continue
    print("Buscando un odd número", num)

#pass no hace nada, puede ser usada para una sentencia pero el programa no requiere ninguna acción

#while True:
#   pass

#se usa para crear clases en su minima expresion.

#class MiClaseLimpia:
#    pass

#Otro lugar donde se puede usar pass es como una marca de lugar para una función o un cuerpo condicional cuando estás trabajando en código nuevo, lo cual te permite pensar a un nivel de abstracción mayor. El pass se ignora silenciosamente:

#def initlog(*args):
#    pass

#match compara expresiones y compara los patrones sucesivos en uno o más bloque de casos.
"""
def http_error(status):
    match status:
        case 400:
            return "Mala recepcion"
        case 404:
            return "No funciona"
        case 418:
            return "Soy un té"
        case _:
            return "A veces es solo un error de internet"
"""
#Observa el último bloque: el «nombre de variable» _ funciona como un comodín y nunca fracasa la coincidencia. Si ninguno de los casos case coincide, ninguna de las ramas es ejecutada.

#Es posible unir variables / ligarlas

match point:
    case(0,0):
        print("Origin")
    case(0,y):
        print(f"Y={y}")
    case(x , 0):
        print(f"X={x}")
    case (x,y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("No es un punto")


#Observa éste con cuidado! El primer patrón tiene dos literales y puede considerarse una extensión del patrón literal que se mostró anteriormente. Pero los siguientes dos patrones combinan un literal y una variable, y la variable liga uno de los elementos del sujeto (point). El cuarto patrón captura ambos elementos, lo que lo hace conceptualmente similar a la asignación que desempaqueta (x, y) = point.

Si estás usando clases para estructurar tus datos, puedes usar el nombre de la clase seguida de una lista de argumentos similar a la de un constructor, pero con la capacidad de capturar atributos en variables:
class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")    
        case _:
            raise ValueError("No es un punto")



