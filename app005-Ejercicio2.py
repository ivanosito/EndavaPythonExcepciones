try:
    print("alpha"[23])
except ZeroDivisionError:
    print("Error: División por cero")
except IndexError:
    print("Error: Índice fuera de rango")
except:
    print("Error desconocido")