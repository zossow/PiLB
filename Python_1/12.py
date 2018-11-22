import random
wymiar = 128
X = [[random.randint(1,1000) for a in range(wymiar)] for a in range(wymiar)]
Y = [[random.randint(1,1000) for b in range(wymiar)] for b in range(wymiar)]
result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
    print(r)
