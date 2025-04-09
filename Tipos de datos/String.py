# String:
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


# Los strings son Arrays: los strings en python son arrays de bytes, los cuales representan un caractér. Esto significa
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


# Para poder obtener el largo (length) de un texto o string usamos len(), el cual recibe como parametro la variable donde
# esta guardado el texto o un texto en crudo (str). Tené en cuenta que los espacios entre las palabras tambien son un caractér.

x = "hola"
len(x)  # Esto devuelve un numero entero, el cual indica la cantidad de caracteres que tiene el string(indica el largo/length)
# Muestra por consola: 4

# Podemos buscar una cadena de texto o un caracter dentro de un string con "in", el cual devuelve un booleano, la sintaxis es la siguiente "string" in variable
txt = "hola mundo"
# String in Variable
# "hola" in txt
"hola" in txt # Esto devuelve True, ya que la cadena de texto "hola" si existe en la variable txt


# Tambien podemos verificar si una texto o caracter NO se encuentra dentro de un string, para esto utilizamos la palabra clave "not"
# antes del "in", despues la sintaxis es la misma

txt = "hola mundo"
"hola" not in txt # Esto devuelve False, ya que la cadena de texto "hola" SI existe en la variable txt
"pedro" not in txt # Esto devuelve True, ya que la cadena de texto "pedro" NO existe en la variable txt

