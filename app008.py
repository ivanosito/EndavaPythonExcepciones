# Propagación de excepciones
def dividir():
    return 10 / 0   # genera ZeroDivisionError

try:
    dividir()
except ZeroDivisionError:
    print("Error capturado fuera de la función")