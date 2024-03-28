import numpy as np

def factorial(n):
    """Computes factorial of numbers. To be used in estimate_pi()"""
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
    
def estimate_pi(max_k):
    """Finds summation of formula by increasing k as long as it is within range(max_k).
    According to the formula exercise 7.3, the value will be 1/ the value * the total
    summation.
    """
    k = np.arange(max_k)
    total = 0
    
    #2sqrt2/9801 value
    value = 2* np.sqrt(2) / 9801
    
    formula = (factorial(4 * k) * (1103 + 26390 * k)) / ((factorial(k)**4) * 396**(4 * k))
    total = np.sum(formula)   

    return 1/(value* total)

#Unit test
def test_estimate_pi():
    # Test with max_k = 1
    result = estimate_pi(1)
    assert np.allclose(result, np.pi)