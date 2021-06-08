def DivDif(XArray):
  n = len(XArray)
  A = [[0.0 for i in range (n)] for
  j in range (n)]
  for i in range(n):
    A[i][0] = f(XArray[i])
  for j in range(1, n):
    for i in range(0, n - j):
      A[i][j] = (A[i+1][j-1] - A[i][j-1])/(XArray[i+j] - XArray[i])
  for i in range(n):
    print(A[i])


def f(x):
  return x**2 + x + 3

DivDif([1.0, 2.0, 3.0])
DivDif([0.0, 0.5, 1.0])