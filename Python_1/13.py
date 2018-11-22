import random
wymiar = 8
X = [[random.randint(1,100) for a in range(wymiar)] for a in range(wymiar)]
Y = [[random.randint(1,100) for b in range(wymiar)] for b in range(wymiar)]
result = [[0 for x in range(wymiar)] for y in range(wymiar)]
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

print(X)
print('\n')
print(Y)
print('\n')
for r in result:
   print(r)
