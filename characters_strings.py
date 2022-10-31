#Cadenas de caracteres

#Además de números, Python puede manipular cadenas de texto, las cuales pueden ser expresadas de distintas formas. Pueden estar encerradas en comillas simples ('...') o dobles ("...") con el mismo resultado 2. \ puede ser usado para escapar comillas:

'spam eggs' #single
'doesn\'t' #single quote debajo
"doesn't"
'"Yes," they said.'
"\"Yes, \" they said."
'"Isn\'t," they said.'

#Las cadenas se pueden concatenar (pegar juntas) con el operador + y se pueden repetir con *:
concatenacion =  3 * 'un'+ 'ium'
print(concatenacion)

#Dos o más cadenas literales (es decir, las encerradas entre comillas) una al lado de la otra se concatenan automáticamente.

python = 'py' 'thon'
print(python)

#Esto solo funciona con dos literales, no con variables ni expresiones.
#Si quieres concatenar variables o una variable y un literal, usa +:

prefix = 'Py'
print(prefix + 'thon')

#Las cadenas de texto se pueden indexar (subíndices), el primer carácter de la cadena tiene el índice 0. No hay un tipo de dato diferente para los caracteres; un carácter es simplemente una cadena de longitud uno:
#La función incorporada len() retorna la longitud de una cadena
word = 'Sebastian'
len(word)


#Cadenas de caracteres — str
#    Las cadenas de texto son ejemplos de tipos secuencias y soportan las operaciones comunes para esos tipos.

#Métodos de las cadenas de caracteres
#    Las cadenas de texto soportan una gran cantidad de métodos para transformaciones básicas y búsqueda.

#Literales de cadena formateados
#    Literales de cadena que tienen expresiones embebidas.

#Sintaxis de formateo de cadena
#    Aquí se da información sobre formateo de cadenas de texto con str.format().

#Formateo de cadenas al estilo *printf*
#    Aquí se describen con más detalle las antiguas operaciones para formateo utilizadas cuando una cadena de texto está a la izquierda del operador %.

