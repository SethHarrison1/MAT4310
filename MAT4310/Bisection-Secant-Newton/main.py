import math as m
def bisection(a, b, max_its, tol, f):
  fa = f(a)
  fb = f(b)
  if fa*fb > 0:
    return
  d = b - a
  for its in range(1, max_its+1):
    d = d/2
    m = a+d
    fm = f(m)
    print(m)
    if fm == 0 or abs(d)  < tol:
      print("convergence")
      print(its)
      return
    if fa * fm > 0:
      a = m
      fa = fm
    else:
      b = m
      fb = fm

def f(x):
  return m.exp(0.2*x) - (x**2)

def secant(a, b, max_its, tol, f):
  fa = f(a)
  fb = f(b)
  if abs(fa) > abs(fb):
    temp = a
    a = b
    b = temp
    temp2 = fa
    fa = fb
    fb = temp2
  for its in range(1, max_its+1):
    d = (b-a)/(fb-fa)
    b = a
    fb = fa
    d = d*fa
    a = a-d
    fa = f(a)
    print(a)
    if fa == 0 or abs(d) < tol:
      print("convergence")
      print(its)
      return  
    if abs(fa) > abs(fb):
      temp3 = a
      a = b
      b = temp3
      temp4 = fa
      fa = fb
      fb = temp4

def fp(x):
  return (0.2 * m.exp(0.2 * x)) - (2*x)
  

def newton(x, max_its, tol, f, fp):
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

newton(-5, 100, 10 ** -10, f, fp)
newton(0, 100, 10 ** -10, f, fp)
newton(1, 100, 10 ** -10, f, fp)
newton(30, 100, 10 ** -10, f, fp)

secant(-5, 0, 100, 10**-10, f)
secant(0, 5, 100, 10 ** -10, f)
secant(30, 40, 100, 10**-10, f)

bisection(-5, 0, 100, 10**-10, f)
bisection(0, 5, 100, 10 ** -10, f)
bisection(30, 40, 100, 10**-10, f)