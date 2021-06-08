import math

def f(x):
  return (x-1)*(x-2)*(x-3)*(x-4)*(x-5)*(x-6)*(x-7.0000000001) #function for which root is desired

def LE_brent(a,b,relerr, abserr):
# Calculates the root of an externally provided function f(x)
# in the interval [a,b]
# with specified relative and absolute error tolerances.
    max_func_evals = 500 #the user should change this value if more evaluations are desired 

    #calculate machine epsilon and make sure tolerance is not too small
    epsilon = 1.0
    while 1 + epsilon > 1.0:
         epsilon = epsilon / 2.0
    epsilon = 2.0 * epsilon
    if ((relerr < 10.0*epsilon) or (abserr < 0.0)):
        print("Error in specifying the tolerances.")
        return

    fb = f(b)
    fa = f(a)
    num_func_evals = 2
    initial_residual = fb
    quad = 0
    lin = 0

    while num_func_evals < max_func_evals:
        # use midpoint as third point
        c = a + (b-a)/2.0
        fc = f(c)
        if fa != fc and fb != fc:  #quadratic interpolation
            s = (a*fb*fc)/((fa-fb)*(fa-fc)) + (b*fa*fc)/((fb-fa)*(fb-fc)) + (c*fa*fb)/((fc-fa)*(fc-fb))
            quad +=1
        else:   # linear (secant) interpolation
            s = b - fb * (b-a) / (fb-fa)
            lin +=1
        fs = f(s)
        num_func_evals += 2
        
        #arrange points to keep root between a and b
        if c > s:
            temp = c
            c = s
            s = temp
            temp = fc
            fc = fs
            fs = temp
        if fc * fs < 0.0:
            a = c
            fa = fc
            b = s
            fb = fs
        elif fs * fb < 0.0:
            a = s
            fa = fs
        else:
            b = c
            fb = fc

        tol = max(abserr, abs(b)*relerr)
        

        if abs((b-a)/2.0) <= tol:
            if abs(fb) > abs(100.0*initial_residual):
                print("There is a pole at", b)
                return
            else:
                print("The root is", b)
                print("and the function value at the root is", fb)
                print("The number of function evaluations:", num_func_evals)
                print("linear steps:", lin, "quadratic steps:", quad)
                return
        if (num_func_evals >= max_func_evals):
            print("Too much work. The number of function calls was", num_func_evals)
            print("There is a root between:", a, b)
            return
        if abs(fb) ==0.0:
            print(" The root is", b)
            print("and the function value at the root is", fb)
            print(" The number of function evaluations:", num_func_evals)
            print("linear steps:", lin, "quadratic steps:", quad)
            return
    
LE_brent(0.5, 7.5, 1.0*(10**-10), 1.0*(10**-10))
