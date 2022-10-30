from __future__ import division


#Tipos de números


"""""
Los números enteros (ej. 2, 4, 20) tienen tipo int, los que tienen una parte fraccionaria (por ejemplo 5.0, 1.6) tiene el tipo float. Vamos a ver más acerca de los tipos numéricos más adelante en el tutorial.

La división (/) siempre retorna un número decimal de punto flotante. Para hacer floor division y obtener un número entero como resultado puede usarse el operador //; para calcular el resto puedes usar %:
"""""
#División Flotante
division_float = 17 / 3
print(division_float)

#Sin la parte fraccionada es con //
sin_fraccional_part = 17 // 3
print(sin_fraccional_part)

#para sacar el resto de una division se hace con %
resto = 17 % 3
print(resto)

#Division con la suma de su resto
divisor_suma_resto = 5 * 3  + 2
print(divisor_suma_resto)

#Potencia con el signo **
cuadrado = 5 ** 2
print(cuadrado)

#Potencia elevada a la 7
elevado_al_siete = 2 ** 7
print(elevado_al_siete)

#El signo igual (=) se usa para asignar un valor a una variable. Ningún resultado se mostrará antes 
#del siguiente prompt interactivo:

width = 20
height = 5 * 9
ancho_alto=  width * height
print(ancho_alto)

#Hay soporte completo de punto flotante; operadores con operando mezclados convertirán los enteros a punto flotante:
a = 4 * 3.75 - 1
print(a)
