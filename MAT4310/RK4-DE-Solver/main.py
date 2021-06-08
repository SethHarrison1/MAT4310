def RK4(a, b, x, n):
  h = (b - a)/n
  t = a
  for i in range(1, n+1):
    k1 = h * f(t, x)
    k2 = h * f(t + (h/2), x + (k1/2))
    k3 = h * f(t + (h/2), x + (k2/2))
    k4 = h * f(t + h, x + k3)
    x = x + (k1 + (2 *(k2 + k3) + k4))/6
    t = a + (i * h)
    print(t, x)

def f(x, t):
  return (10 * x) + (11 * t) - (5 * t**2) - 1

RK4(0, 3, 0, 100)
