def cool(a):
  x = a / 2
  for k in range(1, 51):
    x = ((x*x)+a) / (2.0*x)
  print(x)

cool(1)
cool(2)
cool(45)
cool(100)