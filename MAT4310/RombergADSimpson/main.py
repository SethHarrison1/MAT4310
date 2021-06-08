import math
def f(x):
  return 10*(x**2)*math.exp(-2*x)

def Romberg(a, b, n):
  r = [[0.0 for i in range (n+1)] for
  j in range (n + 1)]
  h = b-a
  r[0][0] = (h / 2) * (f(a) + f(b))
  for i in range(1, n+1):
    h = h/2
    sum = 0
    for k in range(1, 2**i, 2):
      sum = sum + f(a + (k*h))
    r[i][0] = (1/2)* r[i - 1][0] + (sum*h)
    for j in range(1, i+1):
      r[i][j] = r[i][j-1] + (r[i][j-1] - r[i-1][j-1])/((4**j)-1)
  print("R(0,0):", r[0][0])
  print("R(1,0):", r[1][0])
  print("R(1,1):", r[1][1])
  print("R(2,0):", r[2][0])
  print("R(2,1):", r[2][1])
  print("R(2,2):", r[2][2])
  print("R(3,0):", r[3][0])
  print("R(3,1):", r[3][1])
  print("R(3,2):", r[3][2])
  print("R(3,3):", r[3][3])
  print("R(4,0):", r[4][0])
  print("R(4,1):", r[4][1])
  print("R(4,2):", r[4][2])
  print("R(4,3):", r[4][3])
  print("R(4,4):", r[4][4])
  print("R(5,0):", r[5][0])
  print("R(5,1):", r[5][1])
  print("R(5,2):", r[5][2])
  print("R(5,3):", r[5][3])
  print("R(5,4):", r[5][4])
  print("R(5,5):", r[5][5])

Romberg(0,10,5)

def ADSimpson(a, b, eps, level, level_max):
  level = level + 1
  h = b-a
  c = (a+b)/2
  one_simp = h*(f(a) + (4 * f(c)) + f(b))/6
  d = (a + c)/2
  e = (c+b)/2
  two_simp = h*(f(a) + (4 * f(d)) + (2 * f(c)) + (4 * f(e)) + f(b))/12
  if (level >= level_max):
    print("max level reached")
    return(two_simp)
  else:
    if (abs(two_simp - one_simp) < (15 * eps)):
      return(two_simp + (two_simp - one_simp)/15)
    else:
      left_simpson = ADSimpson(a, c, eps / 2, level, level_max)
      right_simpson = ADSimpson(c, b, eps/2, level, level_max)
      return(left_simpson + right_simpson)

print("The integral =", ADSimpson(0, 10, 10**(-10), 0, 10))