import math

def f(x):
	return x**5 -3*x +2# function declaration needed

def adaptiveGK7_15(a, b, epsilon, level_max):
# Adaptive Gauss Kronrod 7-15 method for estimating the integral of a
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

    #build the 7 function values for the classical G7 estimate
    h = 0.5 * (right - left)
    midpoint = left + h
    f1 = f(midpoint - h*0.949107912342759)
    f2 = f(midpoint - h*0.741531185599394)
    f3 = f(midpoint - h*0.405845151377397)
    f4 = f(midpoint)
    f5 = f(midpoint + h*0.405845151377397)
    f6 = f(midpoint + h*0.741531185599394)
    f7 = f(midpoint + h*0.949107912342759)
    q7 = 0.129484966168870*(f1+f7) + 0.279705391489277*(f2+f6)
    q7 += 0.381830050505119*(f3+f5) + 0.417959183673469*f4
    q7 *= h

    #use the 7 function values from above and 8 more to produce K15
    k15 = 0.063092092629979*(f1+f7) + 0.140653259715525*(f2+f6) + 0.190350578064785*(f3+f5) + 0.209482141084728*f4
    k15 += 0.022935322010529*(f(midpoint - h*0.991455371120813) + f(midpoint + h*0.991455371120813))
    k15 += 0.104790010322250*(f(midpoint - h*0.864864423359769) + f(midpoint + h*0.864864423359769))
    k15 += 0.169004726639267*(f(midpoint - h*0.586087235467691) + f(midpoint + h*0.586087235467691))
    k15 += 0.204432940075298*(f(midpoint - h*0.207784955007898) + f(midpoint + h*0.207784955007898))
    k15 *= h
    num_f_eval +=15

    #determine whether to stop or continue
    if level >= level_max:
        print("warning: maximum level exceeded without convergence")
        raise SystemExit(0)
    elif 200*abs(k15-q7)**(1.5) < epsilon:  #error is small enough to return an answer
        return k15
    else:  #subdivide and continue
        left_GK = GaussKronrod(left, left+h, epsilon/2.0, level, level_max)
        right_GK = GaussKronrod(left+h, right, epsilon/2.0, level, level_max)
        return left_GK + right_GK

#customize this call:
adaptiveGK7_15(-1, 1, 10**-10, 50)
                