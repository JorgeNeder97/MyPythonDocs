# STRING:
# El tipo de dato string se pone entre comillas simples o dobles y equivale a texto

x = "hello"
y = 'hello'

# Podemos poner comillas dentro del texto siempre y cuando no sean las mismas que generan el string
# Esto es válido: "Hola 'mundo' "  o  'Hola "mundo" '
# Esto no es válido: "Hola "mundo" "  o  'Hola 'mundo' '

x = "Hola 'mundo'"
y = 'Hola "mundo"'

# Podemos escribir un string con saltos de linea utilizando la triple comilla (simples o dobles) para generar el string
x = """Este string
Tiene saltos de 
Linea"""

y = '''Este string
Tiene saltos de
Linea'''


# LOS STRINGS SON ARRAYS: los strings en python son arrays de bytes, los cuales representan un caractér. Esto significa
# que podemos utilizar los metodos de array en los strings.

# x = "hola"  puede ser tratado como  x = ["h", "o", "l", "a"]
x = "hola"
x[1] # Esto devuelve "o" (recuerda que en los arrays la primera posición corresponde al numero 0, en este caso 0 es la posicion de "h")


# Como los strings son arrays de caracteres, podemos recorrerlos con un bucle como for por ejemplo
x = "hola"
for x in "hola":
    x   #Aqui usariamos print(x) para mostrar por consola cada letra

# El codigo anterior (con print()) muestra por consola 1 print por cada letra:

# Por consola muestra:
# h
# o
# l
# a



# Para poder OBTENER el LARGO (length) de un texto o string usamos len(), el cual recibe como parametro la variable donde
# esta guardado el texto o un texto en crudo (str). Tené en cuenta que los espacios entre las palabras tambien son un caractér.

x = "hola"
len(x)  # Esto devuelve un numero entero, el cual indica la cantidad de caracteres que tiene el string(indica el largo/length)
# Muestra por consola: 4

# Podemos BUSCAR una CADENA de texto O un CARACTÉR dentro de un string con "in", el cual devuelve un booleano, la sintaxis es la siguiente "string" in variable
txt = "hola mundo"
# String in Variable
# "hola" in txt
"hola" in txt # Esto devuelve True, ya que la cadena de texto "hola" si existe en la variable txt


# Tambien podemos VERIFICAR si una TEXTO o CARACTÉR NO SE ENCUENTRA dentro de un string, para esto utilizamos la palabra clave "not"
# antes del "in", despues la sintaxis es la misma

txt = "hola mundo"
"hola" not in txt # Esto devuelve False, ya que la cadena de texto "hola" SI existe en la variable txt
"pedro" not in txt # Esto devuelve True, ya que la cadena de texto "pedro" NO existe en la variable txt


# ------------ Slice Strings --------------------


# Podemos OBTENER una PARTE DE UNA CADENA de texto utilizando la sintaxis de slice.
# Sintaxis: variable(texto)[indice de inicio (incluido): indice de fin (no lo incluye)]
x = "Hola"
x[1:3] # Esto devuelve el texto "ol"

# Si quiero OBTENER el texto HASTA EL FINAL debo indicar un indice adicional al final
# Ej: el texto "Hola" tiene los siguientes indices 0:H, 1:o, 2:l, 3:a
# Para obtener todo el texto hasta el final se haría de la siguiente forma
x[0:4] # Esto devuelve "Hola" (si no entendiste debes ver entornos abiertos y cerrados en matemáticas)

# Existen otras dos formas de utilizar slice:

# OBTENER una parte de la cadena DESDE EL COMIENZO
x[:3] # Esto devuelve Hol

# OBTENER una parte de la cadena desde un indice HASTA EL FINAL
x[1:] # Esto devuelve ola


# Tambien podemos OBTENER una porcion del texto PASANDO INDICES NEGATIVOS
# Cuando se pasan indices negativos los indices empiezan desde el -1, ya que
# el 0 es neutro, no podemos escribir -0.
# Además, cuando utilizamos indices negativos el indice -1 corresponde al ultimo
# caractér del texto y el indice mas alto al primero.
x = "Hola"
x[-3:-1] # Esto devuelve "ola"

# SIEMPRE el primer numero debe ser mayor al segundo, caso contrario devuelve un error de sintaxis.



# ------------ Modify Strings --------------------



# CONVERTIR texto a MINÚSCULA: variable.lower()
# CONVERTIR texto a MAYÚSCULA: variable.upper()
x = "Hola mundo"
x.lower() # Esto devuelve "hola mundo"
x.upper() # Esto devuelve "HOLA MUNDO"


# REMOVER ESPACIOS al comienzo y al final del string: variable.strip()
x = " Hola "
x.stripe() # Devuelve "Hola"


# Para REEMPLAZAR un CARACTÉR por otro en un string utilizamos: variable.replace("caractér a reemplazar", "caractér a insertar")
x = "Tapa"
x.replace("T", "P") # Esto devuelve "Papa"

# si se le pasa un caractér inexistente devuelve el string original



# Para DIVIDIR el texto en un array de textos se utiliza: variable.split("caractér por el cual queremos dividir")
# (un espacio es un caractér)
x = "Hola, mundo"
y = "Como Estas"
x.split(",") # devuelve un array: ["Hola", "mundo"]
y.split(" ") # devuelve un array: ["Como", "Estas"] en este caso dividimos el texto por los espacios en blanco



# Para CONCATENAR dos cadenas de texto utilizamos el operador "+"
x = "Hola "
y = "mundo"
z = x + y # z devuelve "Hola mundo"

# Otro ejemplo:
x = "Hola" + " " + "mundo" # x devuelve "Hola mundo"



# ------------ Format Strings --------------------


# Los strings no pueden ser concatenados con numeros
# Si queremos combinar un numero con un texto debemos formatear el string

# Para esto existen los F STRING, estos permiten insertar variables de tipo numericas o numeros
# dentro de una cadena de texto

precio = 22
texto = "El precio es: "

# En este caso no podemos hacer precio + texto
# La sintaxis de los F String es la siguiente: f"aqui va el texto {aqui va la variable o el numero} mas texto"

mensaje = f"El precio es: {precio}" # Esto devuelve "El precio es: 22"


# Podemos agregar modificadores o realizar operaciones dentro de las llaves
# Los modificadores se agregan con ":" segudo de un modificador válido (ver modificadores en w3school o en la documentación oficial de python)
# Ejemplo de modificador:

mensaje = f"El precio es: {precio:.2f}" # Este modificador convierte a float (con 2 decimales) el dato y devuelve "El precio es: 22.00"

# Ejemplo de operación:
mensaje = f"El precio es: {20 * 2}" # Esto devuelve "El precio es: 40"





# ------------------ Escape Characters ----------------------

# Un escape character es una barra invertida \ seguida de un caractér válido (ver caracteres válidos en: https://www.w3schools.com/python/python_strings_escape.asp)
# Esto nos permite realizar distintas cosas, como poder ingresar comillas dobles "" dentro de un string de comillas dobles "Hola"
# Ej:
# Esto es incorrecto: "Hola "mundo""
# Esto es correcto: "Hola \"mundo\""

# Esto nos permite hacer un salto de linea en un string: \n

# Ver todos los escape characters de python: https://www.w3schools.com/python/python_strings_escape.asp




# ------------------ Métodos de Strings ----------------------

#



# capitalize(): Convierte la primera letra a mayuscula
# casefold()	Convierte el string a minuscula
# center(n)	Recibe un numero (n) como parametro y retorna el string con n espacios atras y adelante 
# count()	Recibe como parametro un caractér, devuelve el numero de veces que ese caractér se repite en el texto
# encode()	Recibe como parametro el metodo de encoding (por defecto es UTF-8), sirve para cambiar el encode del texto
# endswith()	Recibe como parametro un caractér y devuelve true si el texto termina con ese caractér.
# expandtabs()	Si el texto tiene el caractér especial tab \t este metodo nos permite hacer un espacio por cada tab, la cantidad de espacio se determina por el numero que le pasemos como parametro.
# format()	Es una forma verbosa de formatear el string (Recomendación: usar los f string ej: f"Hola {variable}").
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
