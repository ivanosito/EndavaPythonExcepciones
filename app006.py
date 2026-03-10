# Calcula el número de excepciones que hay en Python.
import builtins

exceptions = [
    obj for obj in vars(builtins).values()
    if isinstance(obj, type) and issubclass(obj, BaseException)
]

print(len(exceptions))