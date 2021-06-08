import math as m
def Jacobi(A, b, max_its, tol):
  n = len(b)
  x = [0.0, 0.0, 0.0, 0.0]
  xnew = [0.0, 0.0, 0.0, 0.0]
  for its in range(1, max_its+1):
    for i in range(0, n):
      s = b[i]
      for j in range(0, i):
        s= s - A[i][j] * x[j]
      for j in range(i+1, n):
        s= s - A[i][j] * x[j]
      xnew[i] = s / A[i][i]
    print(xnew)
    S = 0
    for i in range(0, n):
      S+= (xnew[i] - x[i])**2
    if m.sqrt(S) < tol:
      print("Convergence")
      print(xnew)
      print(its)
      return
    else:
      for i in range(n):
        x[i] = xnew[i]
  
A = [[5,1,1,0],[4,1,22,5],[-2,0,12,0],[1,-4,3,15]]
b = [7,32,10,15]
Jacobi(A, b, 100, 10**-10)

def GS(A, b, max_its, tol):
  n = len(b)
  x = [0.0,0.0,0.0,0.0]
  xnew = [0.0, 0.0, 0.0, 0.0]
  for its in range(1, max_its+1):
    for i in range(0, n):
      s = b[i]
      for j in range(0, i):
        s = s - A[i][j] * xnew[j]
      for j in range(i + 1, n):
        s = s - A[i][j] * xnew[j]
      xnew[i] = s / A[i][i]
    print(xnew)
    S = 0
    for i in range(0, n):
      S+= (xnew[i] - x[i])**2
    if m.sqrt(S) < tol:
      print("Convergence")
      print(xnew)
      print(its)
      return
    else:
      for i in range(n):
        x[i] = xnew[i]

GS(A, b, 100, 10**-10)

A2 = [[1, 1, 1, 1, 1], [1, 3, 3**2, 3**3, 3**4], [1, 7, 7**2, 7**3, 7**4], [1, 10, 10**2, 10**3, 10**4], [1, 14, 14**2, 14**3, 14**4]]
b2 = [22, 1, -2, 12, -2]

GS(A2, b2, 100, 10**-10)