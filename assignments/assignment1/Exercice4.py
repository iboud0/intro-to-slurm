import math

def delta(a, b, c):
    return b**2-4*a*c

def roots(a, b, c):
    d = delta(a, b, c)
    if d > 0:
        return (-b+math.sqrt(d))/(2*a), (-b-math.sqrt(d))/(2*a)
    elif d == 0:
        return -b/(2*a)
    else:
        return "No solution in the space of real numbers"