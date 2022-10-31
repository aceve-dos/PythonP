#Por supuesto, podemos usar Python para tareas más complicadas que sumar dos y dos. Por ejemplo, podemos escribir una parte inicial de la serie de Fibonacci <https://en.wikipedia.org/wiki/Fibonacci_number>`_ así:

#la suma de dos elementos define el proximo

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


#La primera línea contiene una asignación múltiple: las variables a y b obtienen simultáneamente los nuevos valores 0 y 1. En la última línea esto se usa nuevamente, demostrando que las expresiones de la derecha son evaluadas primero antes de que se realice cualquiera de las asignaciones. Las expresiones del lado derecho se evalúan de izquierda a derecha.

#El bucle while se ejecuta mientras la condición (aquí: a < 10) sea verdadera. En Python, como en C, cualquier valor entero que no sea cero es verdadero; cero es falso. La condición también puede ser una cadena de texto o una lista, de hecho, cualquier secuencia; cualquier cosa con una longitud distinta de cero es verdadera, las secuencias vacías son falsas. La prueba utilizada en el ejemplo es una comparación simple. Los operadores de comparación estándar se escriben igual que en C: < (menor que), > (mayor que), == (igual a), <= (menor que o igual a), >= (mayor que o igual a) y != (distinto a).

#El cuerpo del bucle está indentado: la indentación es la forma que usa Python para agrupar declaraciones. En el intérprete interactivo debes teclear un tabulador o espacio(s) para cada línea indentada. En la práctica vas a preparar entradas más complicadas para Python con un editor de texto; todos los editores de texto modernos tienen la facilidad de agregar la indentación automáticamente. Cuando se ingresa una instrucción compuesta de forma interactiva, se debe finalizar con una línea en blanco para indicar que está completa (ya que el analizador no puede adivinar cuando tecleaste la última línea). Nota que cada línea de un bloque básico debe estar sangrada de la misma forma.

#La función print() escribe el valor de los argumentos que se le dan. Difiere de simplemente escribir la expresión que se quiere mostrar (como hicimos antes en los ejemplos de la calculadora) en la forma en que maneja múltiples argumentos, cantidades de punto flotante y cadenas. Las cadenas de texto son impresas sin comillas y un espacio en blanco se inserta entre los elementos, así puedes formatear cosas de una forma agradable:

i = 256*256
print('el valor de i es de: ',i )

#El parámetro nombrado end puede usarse para evitar el salto de linea al final de la salida, o terminar la salida con una cadena diferente:
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b


#Footer notes

#Debido a que ** tiene una prioridad mayor que `-, -3**2 se interpretará como -(3**2), por lo tanto dará como resultado -9. Para evitar esto y obtener 9, puedes usar (-3)**2.

#A diferencia de otros lenguajes, caracteres especiales como \n tienen el mismo significado con simple('...') y dobles ("...") comillas. La única diferencia entre las dos es que dentro de las comillas simples no existe la necesidad de escapar " (pero tienes que escapar \') y viceversa.