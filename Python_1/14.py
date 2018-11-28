import random
N = random.randint(0, 6)
X = [[random.randint(0, 10) for x in range(N)] for y in range(N)]
print("Wylosowana macierz: ", X)
def liczWyznacznik(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            total += mul * liczWyznacznik(m, sign * matrix[0][i])
        return total

print("Wyznacznik macierzy jest równy: ", liczWyznacznik(X, 1))
