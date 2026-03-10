# 🐍 Python Exceptions — Endava Study Group

![Python](https://img.shields.io/badge/Python-Exceptions-blue)
![Status](https://img.shields.io/badge/Status-Learning-green)
![License](https://img.shields.io/badge/Philosophy-EAFP-orange)

> “Lo que pueda fallar, fallará.  
> Y lo que no… **¡lo intentará!**”  
> — *Ley de Murphy*

---

## 🎓 About this Repository

This repository contains the **Python example programs** used in the presentation:

## **Python Exceptions**
**Sesión 11 — Grupo de Estudio Python PCAP**

The goal is to explore how Python deals with **errors during runtime**, how to **interpret tracebacks**, and how to **control program flow using exceptions**.

In short:

> 💡 *Errar es humano… pero capturar la excepción es divino.*

---

## 📚 Topics Covered

The examples in this repository correspond to the topics presented in the slides:

- 🔎 What is an Exception
- 📜 Reading a Traceback
- 🛑 Preventing program crashes
- 🎯 Handling specific exception types
- 🌳 The Exception hierarchy
- 🧠 Inspecting the Exception object
- ⬆️ Exception propagation (call stack unwinding)
- 🚀 Forcing propagation with `raise`
- 🧪 Detecting bugs with `assert`
- 🧩 Choosing the correct `except` blocks

---

## 🧠 Philosophy Behind Python Exceptions

Python strongly follows the principle:

### **EAFP**
**Easier to Ask Forgiveness than Permission**

Instead of checking everything beforehand:

```python
if key in dictionary:
    value = dictionary[key]
````

Python encourages:

```python
try:
    value = dictionary[key]
except KeyError:
    value = None
```

This leads to code that is often **cleaner and more Pythonic**.

---

## 📂 Repository Structure

Each file corresponds to a small **demonstration program** used in the presentation.

Example structure:

```
app001.py   → Basic exception example
app002.py   → Reading a traceback
app003.py   → try / except
app004.py   → Multiple exception types
app005.py   → Exception hierarchy
app006.py   → Inspecting the Exception object
app007.py   → Propagation of exceptions
app008.py   → Using raise
app009.py   → Using assert
```

Each script demonstrates **one concept clearly and independently**.

---

## 🧩 The Exception Tree (Simplified)

```
BaseException
    │
    └── Exception
            │
            ├── ArithmeticError
            │       └── ZeroDivisionError
            │
            ├── LookupError
            │       ├── IndexError
            │       └── KeyError
            │
            ├── ImportError
            │
            ├── MemoryError
            │
            └── AssertionError
```

Python contains **around 70 built-in exceptions** organized in this hierarchy.

---

## 🔬 Inspecting the Exception Object

One powerful debugging technique is examining the exception object:

```python
except Exception as e:
    print("Tipo:", type(e).__name__)
    print("Mensaje:", e)
    print("Args:", e.args)
```

And if you want the **full traceback**:

```python
import traceback
traceback.print_exc()
```

---

## ⬆️ Exception Propagation

Unhandled exceptions **automatically travel up the call stack** until a matching `except` is found.

This process is called:

### **Call Stack Unwinding**

```
function_c()
   ↓
function_b()
   ↓
function_a()
   ↓
main program
```

The exception climbs this stack until someone catches it.

---

## 🚀 Re-throwing Exceptions with `raise`

Sometimes you want to **handle an exception partially** and still propagate it:

```python
try:
    dividir()
except ZeroDivisionError:
    print("Error detectado")
    raise
```

This lets the exception **continue climbing the call stack**.

---

## 🧪 Assertions: The Programmer’s Friend

Assertions help detect **logical errors during development**.

```python
assert x > 0, "x must be positive"
```

If the assumption is false:

```
AssertionError
```

Assertions are especially useful for **debugging invariants in algorithms**.

---

## 🧠 Famous Quotes About Errors

> “Programs must be written for people to read,
> and only incidentally for machines to execute.”
> — **Harold Abelson**

> “Testing shows the presence, not the absence of bugs.”
> — **Edsger Dijkstra**

> “Errar es humano…
> pero para complicarlo realmente se necesita una computadora.”
> — **Paul Ehrlich**

---

## 🐍 Final Thought

Exceptions are not just errors.

They are **signals** that something unexpected happened.

Handled correctly, they turn a crashing program into a **robust system**.

> “A good programmer is someone who always looks both ways
> before crossing a one-way street.”
> — **Doug Linder**

---

## 👨‍💻 Author

**Adrián Ivanov**

Python Study Group — Endava

---

⭐ If these examples helped you understand Python exceptions better,
feel free to **star the repository**.

---
