import math
def Trap(a,b,n):
  h = (b-a)/n
  T = (f(a) + f(b))/2
  for i in range(1,n):
    T = T + f(a+(i*h))
  T = h * T
  print("The intergal is", T)
def f(x):
  return (.3*x)/(.04 + x**2)
def Simp(a,b,n):
  h = (b-a)/n
  S = f(a)+f(b)
  odd = 0
  even = 0
  for i in range(1,n,2):
    odd = odd + f(a + (i*h))
  for i in range(2,n-1,2):
    even = even + f(a + (i*h))
  S = h *(S + (4 * odd) + (2 * even))/3
  print("The integral is", S)
Simp(0,4,2000)