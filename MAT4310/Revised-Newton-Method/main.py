import math as m

def oldNewton(x, max_its, tol, f, fp):
  fx = f(x)
  for its in range(1, max_its + 1):
    fpx = fp(x)
    if abs(fpx) == 0.0:
      return
    d = fx / fpx
    x = x - d
    fx = f(x)
    print(x)
    if fx == 0 or abs(d) < tol:
      print("Convergence")
      print(its)
      return

def f(x):
  return m.exp(0.2*x) - (x**2)

def fp(x):
  return 0.2 * m.exp(0.2 * x) - (2 * x)


oldNewton(.102, 100, 10 ** -10, f, fp)
oldNewton(.1022, 100, 10 ** -10, f, fp)
oldNewton(.1024, 1000, 10 ** -10, f, fp)
oldNewton(.103, 1000, 10 ** -10, f, fp)
oldNewton(.104, 100, 10 ** -10, f, fp)

def newNewton(x, max_its, tol, mult, f, fp):
  fx = f(x)
  for its in range(1, max_its + 1):
    fpx = fp(x)
    if abs(fpx) == 0.0:
      return
    d = fx / fpx
    x = x - mult * d
    fx = f(x)
    print(x)
    if fx == 0 or abs(d) < tol:
      print("Convergence")
      print(its)
      return

def g(x):
  return (x**3) - (3*(x**2)) + (3*x) - 1 

def gp(x):
  return (3*(x**2)) - (6*x) + 3

newNewton(4, 100, 10 ** -10, 1, g, gp)
newNewton(4, 100, 10 ** -10, 2, g, gp)
newNewton(4, 100, 10 ** -10, 3, g, gp)

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
    P = P * m.sqrt(s)

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

A = [[1, 1, 1, 1, 1], [1, 3, 3**2, 3**3, 3**4], [1, 7, 7**2, 7**3, 7**4], [1, 10, 10**2, 10**3, 10**4], [1, 14, 14**2, 14**3, 14**4]]
b = [22, 1, -2, 12, -2]

GE_SPP(A, b)