import math

def factorial(n):
    """Computes factorial of numbers. To be used in estimate_pi()"""
    while n > 0:
        recursive = factorial(n-1)
        fact = n * recursive
        n = n - 1
        return fact
    return 1


def estimate_pi():
    """Finds summation of formula by increasing k until the formula is less than 1e-15.
    According to the formula exercise 7.3, the value will be 1/ the value * the total
    summation.
    """
    k = 0
    total = 0
    #2sqrt2/9801 value
    value = 2 * math.sqrt(2) / 9801
    #Compute the summation
    while True:
        formula = (factorial(4 * k) * (1103 + 26390 * k)) / ((factorial(k)**4) * 396**(4 * k))
        total = total + formula
        if formula < 1e-15:
            break
        k = k + 1   
        
    return 1/(value * total)

estimate_pi()