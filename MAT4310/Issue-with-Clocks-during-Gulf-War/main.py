def step_calc():
  dt = 0.0
  for i in range(1,10001):
    dt = dt + 1.0/10.0
    dx = 0.0 + i/10.0
    print(dt)
  print(dt)
  print(dx)
step_calc()

def step_calcProblem():
  dt = 0.0
  for i in range(1, 101):
    dt = dt + 1.0/10.0
    print(dt)

#step_calcProblem()