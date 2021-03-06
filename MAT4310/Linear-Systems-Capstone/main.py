import math as math

def GE_SPP(A,b):
  opcount = 0
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
      opcount = opcount + 1
    P = P * math.sqrt(s)
    opcount = opcount + 1

  for k in range(n-1):
    R = 0.0
    for i in range(k, n):
      temp = abs(A[L[i]][k]/S[L[i]])
      opcount = opcount + 1
      if temp > R:
        R = temp
        index = i
    temp = L[index]
    L[index] = L[k]
    L[k] = temp
    for i in range(k+1,n):
      xmult = A[L[i]][k]/A[L[k]][k]
      opcount = opcount + 1
      for j in range (k+1, n):
        A[L[i]][j] = A[L[i]][j] - xmult * A[L[k]][j]
        opcount = opcount + 2
      b[L[i]] = b[L[i]] - xmult * b[L[k]]
      opcount = opcount + 2
  piv = 1
  for i in range(0,n):
    piv = piv * abs(A[L[i]][i])
    opcount = opcount + 1
  Cond = P / piv
  x[n-1] = b[L[n-1]]/A[L[n-1]][n-1]
  for k in range(n-2,-1,-1):
    tot = b[L[k]]
    for j in range(k+1,n):
      tot = tot - A[L[k]][j]*x[j]
      opcount = opcount + 2
    x[k] = tot/A[L[k]][k]
    opcount = opcount + 1
  print(x)
  print(Cond)
  print(L)
  print("operation count:" ,opcount)



a = [[30, 4, 5, -1, 0, -5, -5, 0, -3, -2, -2, 3, -4, 0, 4, -1, 1, 1, 5, 0, 1, 3, 3, -2,
3, -2, 0, -2, 4, -4, -4, -2, 4, -3, 2, -1, 0, -3, 0, -4, -5, 4, 1, 0, -1, 3, 3, 4, -1,
-2], [4, 30, 4, 1, -5, 0, 0, 3, 1, 4, 2, -1, 2, 0, -5, -2, 4, -2, -2, 0, -2, 0, 4, 2, 5,
-1, 0, 5, 2, 4, -1, 0, -5, 4, 0, -1, -1, 0, 0, -3, -1, 3, -1, -5, -2, -2, 1, -2, -2, 2],
[5, 4, 30, 0, -4, 0, -3, 0, -5, -4, 3, 3, 4, 4, 1, 4, -5, 0, 0, -2, -4, -1, 4, 0, 3, 3,
4, -3, 0, 0, -2, -2, -1, 4, 1, 0, 0, 3, 1, 3, -5, 1, 4, 2, 5, -3, -2, 0, -5, 5], [-1, 1,
0, 30, 5, 0, 0, 0, 5, 1, -2, 0, -3, 4, 0, 0, 3, 4, -1, 2, 3, 0, 0, -1, 1, 4, 0, 4, -4, 0,
3, 5, 5, 5, 2, 1, -4, -3, -5, 0, -2, 0, 0, 1, 3, 0, -5, 1, 0, 5], [0, -5, -4, 5, 30, 0,
-4, -2, 0, -2, -5, 5, 0, -4, 0, 0, 3, -1, 5, 5, -4, 4, 5, 5, 0, 0, -4, -2, -1, 0, -5, 0,
4, 0, -5, 1, 3, 2, 5, 0, 0, 2, 4, -5, -3, 0, -2, -4, -3, 2], [-5, 0, 0, 0, 0, 30, 0, 0,
-4, 0, 2, -5, 0, -5, 1, 0, 2, -1, 2, 0, 0, 3, 0, -2, 1, -1, 0, 3, 2, 3, 3, 0, 5, 1, -2,
-5, -4, 0, -1, 0, -5, 0, -5, -2, 0, 2, 1, 0, 3, -3], [-5, 0, -3, 0, -4, 0, 30, 2, -1, -4,
4, 0, -2, 3, 0, -1, 0, 5, 5, 0, 4, 3, 0, 5, 2, 1, 0, 0, 0, 3, -5, 1, 3, -3, -2, -3, -2,
-5, 4, 0, -3, -2, 0, 0, 0, -2, 0, -4, 3, 3], [0, 3, 0, 0, -2, 0, 2, 30, 0, 0, 0, 2, 0, 3,
3, -1, 3, -3, 0, 1, 2, -3, 1, 0, -4, 3, 0, 5, 1, -3, 1, -5, -2, 0, -1, 0, 0, -1, -4, 1, 4,
-3, 3, 0, -3, 0, 0, 0, 3, 0], [-3, 1, -5, 5, 0, -4, -1, 0, 30, 5, 0, 4, 3, -3, 4, 0, -4,
-4, 0, 0, -4, 0, -3, 0, 0, 1, -5, 5, 1, 3, 1, 5, 1, 3, -4, 5, -2, 4, 4, 0, -4, 3, 0, 4, 0,
-3, -1, -2, 0, 0], [-2, 4, -4, 1, -2, 0, -4, 0, 5, 30, 4, 0, 0, -3, 2, 2, -3, -1, -5, 2,
2, 0, 0, -3, 4, 1, 0, 2, 1, -4, -3, 0, -3, 0, -1, -1, -1, 0, -4, 4, -3, 0, -5, 0, 3, -4,
0, 2, 2, 0], [-2, 2, 3, -2, -5, 2, 4, 0, 0, 4, 30, 0, -4, 0, 0, -5, 0, -3, -3, 1, -3, -1,
1, 2, 0, -5, -4, -5, 0, 0, -3, 3, 0, -1, -2, 2, -3, -1, 1, -1, -4, -3, 2, -2, 0, -2, 3, 0,
2, 2], [3, -1, 3, 0, 5, -5, 0, 2, 4, 0, 0, 30, 4, -5, 4, -2, 0, 3, 3, 0, -4, -3, -4, -1,
-5, -4, 0, 0, 0, -1, 0, 4, 2, -5, 0, 0, -4, 4, 0, 0, -3, 5, 3, 5, 2, 0, 0, 3, 3, -2], [-4,
2, 4, -3, 0, 0, -2, 0, 3, 0, -4, 4, 30, -5, -5, 5, -2, -3, 4, -2, 0, 0, 3, 0, 4, 0, -1,
1, 1, -2, -5, 0, 0, -3, 4, 0, 0, 0, 4, -5, -5, 0, -4, 5, -2, -4, -3, -1, 1, -3], [0, 0, 4,
4, -4, -5, 3, 3, -3, -3, 0, -5, -5, 30, 4, 3, 0, -4, 0, 0, -3, -3, 4, 0, 0, -1, 0, 4, 1,
1, 2, 0, 2, -3, 4, -1, -2, -4, 0, 5, 3, 1, -4, 4, 0, 1, 1, 0, 0, 4], [4, -5, 1, 0, 0, 1,
0, 3, 4, 2, 0, 4, -5, 4, 30, 2, 2, 0, 0, 2, -3, 0, 2, 0, 1, 0, -4, -3, -2, -4, 5, -4, 4,
0, 5, 0, -5, 4, -3, 5, -4, 0, 4, 5, -4, 0, 1, -4, 4, 0], [-1, -2, 4, 0, 0, 0, -1, -1, 0,
2, -5, -2, 5, 3, 2, 30, 5, -3, 0, 1, 0, 3, 0, -2, -5, -4, 3, 2, -4, 1, 0, -4, -4, 4, 0,
5, 0, 0, -5, -5, 0, 0, 1, 0, 0, 1, -1, 0, 0, 5], [1, 4, -5, 3, 3, 2, 0, 3, -4, -3, 0, 0,
-2, 0, 2, 5, 30, 4, 0, 0, 0, 4, -2, -1, 0, -5, -2, 4, 0, 4, 1, -1, 0, -4, 0, 3, -4, 4,
-5, 0, -4, 4, 1, 3, 0, 2, -2, 0, -4, 0], [1, -2, 0, 4, -1, -1, 5, -3, -4, -1, -3, 3, -3,
-4, 0, -3, 4, 30, 1, -4, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 4, 0, -2, 0, 0, -2, -3,
-2, 0, -5, 0, 1, 0, 3, 0, 0, -5], [5, -2, 0, -1, 5, 2, 5, 0, 0, -5, -3, 3, 4, 0, 0, 0, 0,
1, 30, -1, -1, -2, 5, 5, -3, 5, -4, -1, 5, 5, 5, -4, -2, -1, 0, -1, 0, 0, 3, 3, 2, 4, -5,
3, 1, -4, 0, 5, -5, 1], [0, 0, -2, 2, 5, 0, 0, 1, 0, 2, 1, 0, -2, 0, 2, 1, 0, -4, -1, 30,
0, -3, -3, 1, 1, -2, 1, -2, 0, 3, -1, -4, 0, 0, 4, 0, -2, -3, 5, 2, 4, 4, -1, 5, 0, -4, 3,
-5, 5, 0], [1, -2, -4, 3, -4, 0, 4, 2, -4, 2, -3, -4, 0, -3, -3, 0, 0, 0, -1, 0, 30, 2,
1, 3, -2, 0, 3, 3, 1, 3, -1, 0, -3, -1, 1, 0, 3, 0, -4, 3, 5, 4, 2, 4, -5, -4, 0, 0, 0,
1], [3, 0, -1, 0, 4, 3, 3, -3, 0, 0, -1, -3, 0, -3, 0, 3, 4, 1, -2, -3, 2, 30, 0, 0, 2,
-5, -3, -3, -2, 1, -4, 1, -1, 2, 1, 0, 0, -4, -1, -1, -4, 1, 0, 4, -2, 5, 0, 2, -3, -4],
[3, 4, 4, 0, 5, 0, 0, 1, -3, 0, 1, -4, 3, 4, 2, 0, -2, 2, 5, -3, 1, 0, 30, 4, -5, 5, 0,
0, -2, 2, -2, 0, 5, 1, 0, -2, 1, -4, 0, 5, 0, 1, -4, -3, -4, 4, 5, -4, -3, 5], [-2, 2, 0,
-1, 5, -2, 5, 0, 0, -3, 2, -1, 0, 0, 0, -2, -1, 0, 5, 1, 3, 0, 4, 30, 0, 3, 2, 0, 3, 4,
0, 5, 0, -3, -2, 0, 1, 3, 0, 0, -5, 1, 4, 2, 5, 0, 0, 1, 3, 0], [3, 5, 3, 1, 0, 1, 2, -4,
0, 4, 0, -5, 4, 0, 1, -5, 0, 0, -3, 1, -2, 2, -5, 0, 30, -1, -3, -4, 0, 3, 0, -5, 0, 1,
0, 0, 1, -3, 0, 1, 0, 0, 5, -5, 0, -3, 5, 4, 0, 0], [-2, -1, 3, 4, 0, -1, 1, 3, 1, 1, -5,
-4, 0, -1, 0, -4, -5, 0, 5, -2, 0, -5, 5, 3, -1, 30, 0, -5, -1, 0, -1, -4, 0, 0, -2, 2,
1, 5, 5, 2, 0, -5, 3, -5, 2, 2, -4, -5, -3, -2], [0, 0, 4, 0, -4, 0, 0, 0, -5, 0, -4, 0,
-1, 0, -4, 3, -2, 0, -4, 1, 3, -3, 0, 2, -3, 0, 30, 1, -4, 0, 0, 3, 0, 4, -1, -1, 4, 1,
1, 5, 2, -2, 0, 1, -1, -1, 0, 3, 3, 0], [-2, 5, -3, 4, -2, 3, 0, 5, 5, 2, -5, 0, 1, 4, -3,
2, 4, 0, -1, -2, 3, -3, 0, 0, -4, -5, 1, 30, 3, 0, 0, 5, 1, 4, 4, -3, -2, 4, -5, 2, -2,
-4, 0, 0, 4, 1, 0, 4, 2, 5], [4, 2, 0, -4, -1, 2, 0, 1, 1, 1, 0, 0, 1, 1, -2, -4, 0, 0, 5,
0, 1, -2, -2, 3, 0, -1, -4, 3, 30, 0, 0, 1, -2, 0, 0, 0, -4, 1, -5, 2, 0, 4, -1, 1, 1,
-4, 3, 1, -1, 2], [-4, 4, 0, 0, 0, 3, 3, -3, 3, -4, 0, -1, -2, 1, -4, 1, 4, 0, 5, 3, 3, 1,
2, 4, 3, 0, 0, 0, 0, 30, 4, 0, 0, 5, -4, 0, 2, 1, -1, 3, -1, -1, 5, 0, 2, -3, 0, -3, -2,
0], [-4, -1, -2, 3, -5, 3, -5, 1, 1, -3, -3, 0, -5, 2, 5, 0, 1, 0, 5, -1, -1, -4, -2, 0,
0, -1, 0, 0, 0, 4, 30, 4, 5, 0, -4, -5, -3, 0, 0, -1, -3, -3, 3, 0, 2, 0, -2, 5, -1, 1],
[-2, 0, -2, 5, 0, 0, 1, -5, 5, 0, 3, 4, 0, 0, -4, -4, -1, -2, -4, -4, 0, 1, 0, 5, -5, -4,
3, 5, 1, 0, 4, 30, 5, 4, 5, 3, 4, 1, -1, 0, 1, 5, -3, 3, 1, 0, 0, -3, -4, -1], [4, -5,
-1, 5, 4, 5, 3, -2, 1, -3, 0, 2, 0, 2, 4, -4, 0, 0, -2, 0, -3, -1, 5, 0, 0, 0, 0, 1, -2,
0, 5, 5, 30, -1, -2, 4, 2, 4, -5, -5, -3, 0, 4, -1, 2, 0, 0, 2, 5, 0], [-3, 4, 4, 5, 0,
1, -3, 0, 3, 0, -1, -5, -3, -3, 0, 4, -4, 4, -1, 0, -1, 2, 1, -3, 1, 0, 4, 4, 0, 5, 0, 4,
-1, 30, -3, -5, 3, 0, -3, 2, 4, -4, 1, 5, 0, -1, 2, -4, 5, -2], [2, 0, 1, 2, -5, -2, -2,
-1, -4, -1, -2, 0, 4, 4, 5, 0, 0, 0, 0, 4, 1, 1, 0, -2, 0, -2, -1, 4, 0, -4, -4, 5, -2,
-3, 30, 2, -3, -4, -2, -1, 0, 0, 4, 1, -5, -5, 3, 3, 2, -4], [-1, -1, 0, 1, 1, -5, -3, 0,
5, -1, 2, 0, 0, -1, 0, 5, 3, -2, -1, 0, 0, 0, -2, 0, 0, 2, -1, -3, 0, 0, -5, 3, 4, -5, 2,
30, 0, -1, 0, 4, 5, 0, 5, -3, 4, 0, 0, 5, -4, 1], [0, -1, 0, -4, 3, -4, -2, 0, -2, -1,
-3, -4, 0, -2, -5, 0, -4, 0, 0, -2, 3, 0, 1, 1, 1, 1, 4, -2, -4, 2, -3, 4, 2, 3, -3, 0,
30, 1, -3, 1, 3, 0, -3, -3, 5, 4, 1, -3, -5, -2], [-3, 0, 3, -3, 2, 0, -5, -1, 4, 0, -1,
4, 0, -4, 4, 0, 4, 0, 0, -3, 0, -4, -4, 3, -3, 5, 1, 4, 1, 1, 0, 1, 4, 0, -4, -1, 1, 30,
0, -3, 1, 3, 0, 3, 0, 0, -4, 0, 0, 3], [0, 0, 1, -5, 5, -1, 4, -4, 4, -4, 1, 0, 4, 0, -3,
-5, -5, -2, 3, 5, -4, -1, 0, 0, 0, 5, 1, -5, -5, -1, 0, -1, -5, -3, -2, 0, -3, 0, 30, -5,
0, -4, 0, -4, 3, 3, 1, -1, -2, 5], [-4, -3, 3, 0, 0, 0, 0, 1, 0, 4, -1, 0, -5, 5, 5, -5,
0, -3, 3, 2, 3, -1, 5, 0, 1, 2, 5, 2, 2, 3, -1, 0, -5, 2, -1, 4, 1, -3, -5, 30, -1, 0, 5,
5, 0, 0, 1, 3, 3, 5], [-5, -1, -5, -2, 0, -5, -3, 4, -4, -3, -4, -3, -5, 3, -4, 0, -4, -2,
2, 4, 5, -4, 0, -5, 0, 0, 2, -2, 0, -1, -3, 1, -3, 4, 0, 5, 3, 1, 0, -1, 30, -3, 0, -5,
4, 0, 5, 0, -1, -2], [4, 3, 1, 0, 2, 0, -2, -3, 3, 0, -3, 5, 0, 1, 0, 0, 4, 0, 4, 4, 4, 1,
1, 1, 0, -5, -2, -4, 4, -1, -3, 5, 0, -4, 0, 0, 0, 3, -4, 0, -3, 30, -1, -5, -5, -4, 1,
-1, 2, 0], [1, -1, 4, 0, 4, -5, 0, 3, 0, -5, 2, 3, -4, -4, 4, 1, 1, -5, -5, -1, 2, 0, -4,
4, 5, 3, 0, 0, -1, 5, 3, -3, 4, 1, 4, 5, -3, 0, 0, 5, 0, -1, 30, 0, -3, 0, 4, 0, 3, 3],
[0, -5, 2, 1, -5, -2, 0, 0, 4, 0, -2, 5, 5, 4, 5, 0, 3, 0, 3, 5, 4, 4, -3, 2, -5, -5, 1,
0, 1, 0, 0, 3, -1, 5, 1, -3, -3, 3, -4, 5, -5, -5, 0, 30, 2, 0, 4, 3, 5, 0], [-1, -2, 5,
3, -3, 0, 0, -3, 0, 3, 0, 2, -2, 0, -4, 0, 0, 1, 1, 0, -5, -2, -4, 5, 0, 2, -1, 4, 1, 2,
2, 1, 2, 0, -5, 4, 5, 0, 3, 0, 4, -5, -3, 2, 30, -5, 4, 0, 4, 0], [3, -2, -3, 0, 0, 2,
-2, 0, -3, -4, -2, 0, -4, 1, 0, 1, 2, 0, -4, -4, -4, 5, 4, 0, -3, 2, -1, 1, -4, -3, 0, 0,
0, -1, -5, 0, 4, 0, 3, 0, 0, -4, 0, 0, -5, 30, 0, 0, 4, -4], [3, 1, -2, -5, -2, 1, 0, 0,
-1, 0, 3, 0, -3, 1, 1, -1, -2, 3, 0, 3, 0, 0, 5, 0, 5, -4, 0, 0, 3, 0, -2, 0, 0, 2, 3, 0,
1, -4, 1, 1, 5, 1, 4, 4, 4, 0, 30, 4, -4, 5], [4, -2, 0, 1, -4, 0, -4, 0, -2, 2, 0, 3,
-1, 0, -4, 0, 0, 0, 5, -5, 0, 2, -4, 1, 4, -5, 3, 4, 1, -3, 5, -3, 2, -4, 3, 5, -3, 0, -1,
3, 0, -1, 0, 3, 0, 0, 4, 30, 0, 0], [-1, -2, -5, 0, -3, 3, 3, 3, 0, 2, 2, 3, 1, 0, 4, 0,
-4, 0, -5, 5, 0, -3, -3, 3, 0, -3, 3, 2, -1, -2, -1, -4, 5, 5, 2, -4, -5, 0, -2, 3, -1, 2,
3, 5, 4, 4, -4, 0, 30, 2], [-2, 2, 5, 5, 2, -3, 3, 0, 0, 0, 2, -2, -3, 4, 0, 5, 0, -5, 1,
0, 1, -4, 5, 0, 0, -2, 0, 5, 2, 0, 1, -1, 0, -2, -4, 1, -2, 3, 5, 5, -2, 0, 3, 0, 0, -4,
5, 0, 2, 30]]




b = [ 0.0 for i in range(50)]
for i in range(50):
   for j in range(50):
      b[i] = b[i] + a[i][j]

def GS(A, b, max_its, tol):
  n = len(b)
  x = [0.0] * n
  xnew = [0.0] * n
  opcount = 0
  for its in range(1, max_its+1):
    for i in range(0, n):
      s = b[i]
      for j in range(0, i):
        s = s - A[i][j] * xnew[j]
        opcount = opcount + 2
      for j in range(i + 1, n):
        s = s - A[i][j] * xnew[j]
        opcount = opcount + 2
      xnew[i] = s / A[i][i]
      opcount = opcount + 1
    print(xnew)
    S = 0
    for i in range(0, n):
      S+= (xnew[i] - x[i])**2
      opcount = opcount + 3
    if math.sqrt(S) < tol:
      print("Convergence")
      print(xnew)
      print(its)
      print("opcount:", opcount)
      return
    else:
      for i in range(n):
        x[i] = xnew[i]



GS(a, b, 200, 10**-10)
#GE_SPP(a, b)
