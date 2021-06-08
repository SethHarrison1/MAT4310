def roots(a):
  sx = a/2
  cx = a/3
  max_its = 100
  for its in range(1, max_its):
    sx = (sx/2) + (a/(2*sx))
    cx = (2*cx + (a/(cx**2)))/3
    if (abs(sx**2 - a) < .00001) and (abs((cx**3) - a) < .00001):
      print("The square and cube roots of", a, " are: ", sx, " and ", cx)
      return
roots(4)
roots(10)
roots(64)
roots(1000)