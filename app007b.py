import math
import traceback

try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
except ValueError:
    print("Debes ingresar un número entero válido.")
except Exception as e:
    print("Tipo:", type(e).__name__)
    print("Mensaje:", e)
    print("Args:", e.args)
    print("\nTraceback completo:")
    traceback.print_exc()
print("Programa terminó OK.")