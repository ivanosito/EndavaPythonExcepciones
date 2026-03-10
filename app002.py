# Ejemplo de Traceback
def c():
    return 1 / 0

def b():
    return c()

def a():
    return b()

a()