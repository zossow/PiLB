import math
class Zespolone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = complex(x, y)

    def dodawanie(self, z1, z2):
        z3_real = z1.x + z2.x
        z3_imag = z1.y + z2.y
        z3 = complex(z3_real, z3_imag)
        return z3

    def odejmowanie(self, z1, z2):
        z3_real = z1.x - z2.x
        z3_imag = z1.y - z2.y
        z3 = complex(z3_real, z3_imag)
        return z3

    def modul(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))


a = Zespolone(5, 8)
b = Zespolone(4, 3)
print(a.dodawanie(a, b))
print(a.odejmowanie(a, b))
print(a.modul())
