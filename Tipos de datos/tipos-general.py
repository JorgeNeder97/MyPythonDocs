# DataTypes:
# Los tipos de datos que existen en python son los siguientes:

# Text type: str

# Numeric types: int, float, complex

# Sequences types: list, tuple, range

# Mapping type: dict

# Set types: set, frozenset

# Boolean type: bool

# Binary types: bytes, bytearray, memoryview

# None type: NoneType


# ¿Cómo saber el tipo de dato de una variable? (tambien sirve si pasamos el dato en crudo)
# Para esto existe el comando type() el cual tiene la siguiente sintaxis y devuelve el tipo de dato de la variable que le pasamos como parametro
x = "hola"
type(x) # Esto devuelve "string"



# En las siguientes secciones (en los otros archivos) se muestran los tipos de datos y las funciones pertinentes relacionadas a los mismos.
# Estas funciones sirven para hacer lo que llaman "casting".
# El Casting consiste en tomar una variable o un dato y cambiar el tipo de dato a otro.
# por ejemplo tomamos "2" y lo convertimos de string a entero con int("2")