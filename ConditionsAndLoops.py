import sys

lista = []
for i in range (4738, 9466):
    if i % 2 != 0:
        lista.append(i)

print(sum(lista))
