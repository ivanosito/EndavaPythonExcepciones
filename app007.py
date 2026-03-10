import math

try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
except:
    print("Oh cielos, algo salió mal...")
print("Programa terminó OK.")