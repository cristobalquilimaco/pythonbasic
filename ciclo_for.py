"""Escribe un programa en Python que utilice un ciclo for para hacer lo siguiente:

Imprime los números del 1 al 10 (inclusive) en una sola línea, separados por comas."""

for num in range(1, 11):
    if num < 10:
        print(num, end=",")
    else:
        print(num)


for num in range(1, 11):
    if num <= 10:
        print(num + 1, end=",")
    else:
        print(num)