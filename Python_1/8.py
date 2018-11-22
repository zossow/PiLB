#!/usr/bin/env python3
import random
liczby = []
for x in range(50):
    liczba = random.randint(1, 1000)
    liczby.append(liczba)
print(liczby)
print(len(liczby))
for i in range(len(liczby)-1, 0, -1):
    for liczba in range(i):
        if liczby[liczba+1] > liczby[liczba]:
            y = liczby[liczba]
            liczby[liczba] = liczby[liczba+1]
            liczby[liczba+1] = y
print("Liczby malejąco:", liczby)
