from math import sqrt

def fb(n):
    return ((1 + sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
