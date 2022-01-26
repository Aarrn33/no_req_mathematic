from no_req_mathematic.functions.pgcd import *


def irreductible(x, y):
    """
    Makes it so that x/y is irreductible

    Parameters:
        x: The numerator of the fraction
        y: The denominator of the fraction (can't be 0)

    Returns:
        If the fraction has an integer equivalent:
            int: The franction's equivalent implies that x = k * y where k is a positive integer
        If the fraction hasn't an integer equivalent:
            int: The new numerator
            int: The new denominator
    """
    pgcdx_y = pgcd(x, y)
    if x >= y:
        for k in range(1, int(x/y)+1):
            if x == k * y:
                return k
    return x // pgcdx_y, y // pgcdx_y
