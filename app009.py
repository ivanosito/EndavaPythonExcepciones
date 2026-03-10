# Propagación forzada (raise) de excepciones
def dividir():
    try:
        return 10 / 0
    except ZeroDivisionError:
        print("Capturada dentro de la función")
        raise   # vuelve a lanzar la excepción 
                # para que sea capturada fuera de la función

try:
    dividir()
except ZeroDivisionError:
    print("Capturada fuera")