# Propagación de excepciones
def dividir():
    try:
        return 10 / 0
    except ZeroDivisionError:
        print("Capturada dentro de la función")

try:
    dividir()
except ZeroDivisionError:
    print("Capturada fuera")