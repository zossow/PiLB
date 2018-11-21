#!/usr/bin/env python3
import math
a1,b1,c1 = input("Podaj a,b,c oddzielone spacjami: ").split()
a = float(a1)
b = float(b1)
c = float(c1)
if a == b == c == 0:
    print("Brak rozwiazania")
else:
    if a > 0 or a < 0:
        delta = b ** 2 - (4 * a * c)
        print("Delta = %d" % (delta))
        if delta == 0:
            x0 = -b/(2*a)
            print("Delta=0, rozwiazanie x=%d" % (x0))
        elif delta > 0:
            from math import sqrt

            x1 = (b * b - sqrt(delta) / 4 * a)
            x2 = (b * b + sqrt(delta) / 4 * a)
            print("Rozwiazania x1,x2: x1=%d ; x2=%d" % (x1, x2))
        elif delta < 0:
            print("Delta<0 brak rozwiazania rzeczywistego")
    elif a == 0:
        x = (-c / b)
        print("Wynik x=-%d/%d" % (c, b))
