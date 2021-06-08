A = [[4, 1, 0, 0, 0], [1,4,1,0,0],[0,1,4,1,0],[0,0,1,4,1],[0,0,0,1,4]]
b1 = [5,6,6,6,5]
def buildTri(A, b):
  n = len(b)
  a = [0.0] * (n - 1)
  c = [0.0] * (n - 1)
  d = [0.0] * n
  for i in range(0, n):
    for j in range(0,n):
      if(i == j):
        d[i] = A[i][j]
    for j in range(0, n-1):
      if(i == j):
        c[i] = A[i][j+1]
      if(i == j):
        a[i] = A[i+1][j]
  print("d:", d)
  print("a:", a)
  print("c:", c)
  print("b:", b)

buildTri(A, b1)

a = [1,1,1,1]
d = [4,4,4,4,4]
c = [1,1,1,1]

def tri(a,b,c,d):
  n = len(b)
  x = [0.0] * n
  for i in range(1, n):
    xmult = a[i-1]/d[i-1]
    d[i] = d[i] - xmult * c[i-1]
    b[i] = b[i] - xmult * b[i-1]
  x[n-1] = b[n-1]/d[n-1]
  for i in range(n-2, -1, -1):
    x[i] = (b[i] - c[i] * x[i+1])/d[i]
  print(x)
  
tri(a,b1,c,d)  