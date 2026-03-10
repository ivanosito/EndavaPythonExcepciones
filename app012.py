import math

try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Error: Debes ingresar un número entero")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero")
except:
    print("Error desconocido")
finally:
    print("Programa terminó OK.")