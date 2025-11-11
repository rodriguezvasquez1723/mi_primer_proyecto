# calculadora.py
print("Calculadora básica")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
if b != 0:
    print(f"División: {a / b}")
else:
    print("No se puede dividir entre cero.")
