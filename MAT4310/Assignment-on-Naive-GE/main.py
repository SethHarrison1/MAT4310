def GE(A, b):
  n = len(b)
  X = [0,0,0]
  for k in range(0, n-1):
    for i in range(k+1, n):
      xmult = A[i][k]/A[k][k]
      A[i][k] = xmult
      for j in range(k+1, n):
        A[i][j] = A[i][j] - (A[k][j] * xmult)
      b[i] = b[i] - (xmult * b[k])
  X[n-1] = b[n-1]/A[n-1][n-1]
  for i in range(n-2, -1, -1):
    total = b[i]
    for j in range(i+1, n):
      total = total - (A[i][j] * X[j])
    X[i] = total / A[i][i]
  print(X)



A = [[3,2,-5],[2,-3,1],[1,4,-1]]
b = [2,1,4]
GE(A,b)