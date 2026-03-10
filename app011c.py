# ¿Qué imprime el siguiente código?
def foo(x):
    assert x
    return 1/x
try:
    print(foo(0))
except ZeroDivisionError:
    print("cero")
except AssertionError:
    print("assert")
except:
    print("algo")
