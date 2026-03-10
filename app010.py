# Usando assert para validar que 
# el número ingresado es positivo, 
# de lo contrario se lanzará una excepción AssertionError.

import math
x = float(input("Ingresa un número: "))
# Me aseguro que x es positivo, 
# de lo contrario se lanzará una excepción AssertionError.
assert x >= 0.0, "¡El número debe ser positivo!"
x = math.sqrt(x)
print(x)