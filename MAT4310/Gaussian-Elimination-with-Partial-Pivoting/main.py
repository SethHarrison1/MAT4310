import math
def GE_SPP(A,b):
  n = len(b)
  L = [i for i in range(n)]
  x = [0.0 for i in range(n)]
  S = [0.0 for i in range(n)]
  for i in range(0, n):
    for j in range(0,n):
      if (abs(A[i][j]>S[i])):
        S[i] = abs(A[i][j])
  P = 1
  for i in range(0,n):
    s = 0
    for j in range(0,n):
      s = s + (A[i][j]**2)
    P = P * math.sqrt(s)

  for k in range(n-1):
    R = 0.0
    for i in range(k, n):
      temp = abs(A[L[i]][k]/S[L[i]])
      if temp > R:
        R = temp
        index = i
    temp = L[index]
    L[index] = L[k]
    L[k] = temp
    for i in range(k+1,n):
      xmult = A[L[i]][k]/A[L[k]][k]
      for j in range (k+1, n):
        A[L[i]][j] = A[L[i]][j] - xmult * A[L[k]][j]
      b[L[i]] = b[L[i]] - xmult * b[L[k]]
  piv = 1
  for i in range(0,n):
    piv = piv * abs(A[L[i]][i])
  Cond = P / piv
  x[n-1] = b[L[n-1]]/A[L[n-1]][n-1]
  for k in range(n-2,-1,-1):
    tot = b[L[k]]
    for j in range(k+1,n):
      tot = tot - A[L[k]][j]*x[j]
    x[k] = tot/A[L[k]][k]
  print(x)
  print(Cond)
  print(L)

A = [[5,6,7],[9,1,0],[2,3,4]]
b = [18,10,9]

GE_SPP(A,b)