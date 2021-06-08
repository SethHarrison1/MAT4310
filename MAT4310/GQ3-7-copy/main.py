import math

def f(x):
	return (3 * math.exp(-8*x)*math.cos(x)) + 1 #declare function here

def adaptiveGK3_7(a, b, epsilon, level_max):
# Adaptive Gauss Kronrod 3-7 method for estimating the integral of a
# function f(x) from a to b with error epsilon provided by the user.
# Edit the function definition and the adapt call below to change the problem

    #track the global variable counting the number of function evaluations
    global num_f_eval
    num_f_eval = 0

    #start the recursive method at level 0
    ans = GaussKronrod(a, b, epsilon, 0, level_max)
    print("Gauss Kronrod Integration")
    print("The estimate for the integral is:", ans)
    print("The number of function evaluations is:", num_f_eval)

    
def GaussKronrod(left, right, epsilon, level, level_max):
    global num_f_eval
    level = level + 1

    #build the 3 function values for the classical G3 estimate
    h = 0.5 * (right - left)
    midpoint = left + h
    f1 = f(midpoint - h*0.7745966692414834)
    f2 = f(midpoint)
    f3 = f(midpoint + h*0.7745966692414834)
    q3 = h * (5.0*(f1 + f3) + 8.0 *f2) / 9.0

    #use the 3 function values from above and 4 more to produce K7
    k7 = 0.2684880898683334 * (f1 + f3) + 0.4509165386584744 * f2
    k7 += 0.1046562260264672*(f(midpoint-h*0.9604912687080202) + f(midpoint+h*0.9604912687080202))
    k7 += 0.4013974147759622*(f(midpoint-h*0.4342437493468026) + f(midpoint+h*0.4342437493468026))
    k7 *= h
    num_f_eval +=7

    #determine whether to stop or continue
    if level >= level_max:
        print("warning: maximum level exceeded without convergence")
        raise SystemExit(0)
    elif 200*abs(k7-q3)**(1.5) < epsilon:  #error is small enough to return an answer
        return k7
    else:  #subdivide and continue
        left_GK = GaussKronrod(left, left+h, epsilon/2.0, level, level_max)
        right_GK = GaussKronrod(left+h, right, epsilon/2.0, level, level_max)
        return left_GK + right_GK

#customize this call:
adaptiveGK3_7(0, 2, 10**-10, 50)
                