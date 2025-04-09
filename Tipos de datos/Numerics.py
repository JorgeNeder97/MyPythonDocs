# Numbers:

# Int (Integer): son numeros enteros, positivos y negativos.
x = 0
y = 10234012930
z = -45182930122231298492

# Para convertir un numero a entero usamos int() y pasamos el numero como parámetro
a = int(22.2)


# Float: son numeros decimales positivos y negativos con uno o mas numeros a la derecha del punto
x = 10.0
y = 12304.23
z = -12392489.23192

# Para convertir un numero a decimal usamos float() y pasamos el numero como parámetro
a = float(23)


# Complex: son numeros complejos (positivos y negativos) que tienen una parte imaginaria, la cual se representa con la letra "j"
x = 3+5j
y = 5j
z = -5j

# Para convertir un numero a complex usamos complex() y pasamos el numero como parámetro
a = complex(12)


# Random number:
# Python no tiene una funcion nativa para crear un numero random, pero existe un modulo interno de python llamado random, el cual
# sirve para generar un numero aleatorio (debemos importar este modulo para poder usarlo)
import random

# El modulo random tiene muchos metodos, puedes leer la documentación aquí: https://www.w3schools.com/python/module_random.asp
# Uno de los metodos es randrange(), este recibe 3 parametros (el ultimo es opcional)
# randrange(start, stop, step)
# start indica desde que numero va a tomar un numero aleatorio
# stop indica hasta que numero va a tomar un numero aleatorio
# step hace que saltee la cantidad de numeros que le pases
# En el siguiente ejemplo devuelve un numero aleatorio entre el 1 y el 9 y saltea dos numeros desde el 1 hasta el 9, es decir
# puede mostrar los siguientes numeros: 1, 3, 5, 7 y 9 (se saltea de a 2 numeros, esto hace el parametro step)
random.randrange(1, 9, 2)

# el siguiente ejemplo devuelve un numero cualquiera entre el 1 y el 9
random.randrange(1, 9)