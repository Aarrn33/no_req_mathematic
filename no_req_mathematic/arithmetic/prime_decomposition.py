from no_req_mathematic.arithmetic.smallest_divider import *


def prime_decomposition(n):
    dec = []
    x = n
    while not isprime(x):
        i = smallest_divider(x)
        x = x//i
        dec.append(i)
    dec.append(x)
    return dec
