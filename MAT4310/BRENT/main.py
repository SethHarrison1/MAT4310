import math

def f(x):
  return (x-1)*(x-2)*(x-3)*(x-4)*(x-5)*(x-6)*(x-7.0000000001) #function for which root is desired

def brent(a,b,relerr,abserr):
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


    count = 0
    width = abs(a-b)
    fb = f(b)
    fa = f(a)
    num_func_evals = 2

    if fb == 0.0:  # see if the root is already found
        print(" The root is", b)
        Print("and the function value at the root is", 0.0)
        return
    if fa * fb >= 0.0:  # make sure the root is between the endpoints/
        print("[b,c] does not bracket the root.")
        return
    if abs(fa) < abs(fb):  # keep the value closest to the axis
        temp = a
        a = b
        b = temp
        temp = fa
        fa = fb
        fb = temp
    initial_residual = fa
    c = a
    fc = fa
    mflag = True
    lin = 0
    quad = 0
    while num_func_evals < max_func_evals:
        if fa != fc and fb != fc:  #quadratic interpolation
            s = (a*fb*fc)/((fa-fb)*(fa-fc)) + (b*fa*fc)/((fb-fa)*(fb-fc)) + (c*fa*fb)/((fc-fa)*(fc-fb))
            quad +=1
        else: # linear (secant) interpolation
            s = b - fb * (b-a) / (fb-fa)
            lin +=1
        bisect = False

        #see if we need to switch to bisection 
        if s < (3.0*a + b)/4.0 or s > b:  
            bisect = True
        elif mflag and abs(s-b) >= abs((b-c)/2.0):
            bisect = True
        elif not mflag and abs(s-b) >= abs((c-d)/2.0):
            bisect = True
        elif mflag and abs(b-c) < abserr:
            bisect = True
        elif not mflag and abs(c-d)< abserr:
            bisect = True

        # do bisection if we should
        if bisect:  
            s = a + (b-a)/2.0
            mflag = True
        else:
            mflag = False
        
        #set up for next iteration
        fs = f(s)
        num_func_evals += 1
        d = c
        c = b
        fc = fb
        if fa*fs < 0.0:
            b = s
            fb = fs
        else:
            a = s
            fa = fs
        if abs(fa) < abs(fb):
            temp = a
            a = b
            b = temp
            temp = fa
            fa = fb
            fb = temp

        # check to see if we found a root or a pole or if we did the max function evaluations
        tol = max(abserr, abs(b)*relerr)
        if abs((b-a)/2.0) <= tol:
            if abs(fb) > abs(100.0*initial_residual):
                print("There is a pole at", b)
                return
            else:
                print(" The root is", b, "and the function value at the root is", fb)
                print(" The number of function calls:", num_func_evals)
                print("linear steps:", lin, "quadratic steps:", quad)
                return
        if (num_func_evals >= max_func_evals):
            print("Too much work. The number of function calls:", num_func_evals)
            print("There is a root between:", a, b)
            return
        if abs(fb) ==0.0:
            print(" The root is", b)
            print("and the function value at the root is", fb)
            print(" The number of function calls:", num_func_evals)
            print("linear steps:", lin, "quadratic steps:", quad)
            return

brent(0.5, 7.5, 1.0*(10**-10), 1.0*(10**-10))