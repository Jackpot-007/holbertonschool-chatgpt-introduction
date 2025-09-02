#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) < 2:
    print("Uso: python3 script.py <numero>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    f = factorial(num)
    print(f)
except ValueError as e:
    print("Error:", e)