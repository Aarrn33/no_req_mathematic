from no_req_mathematic.isprime import *


def smallest_divider(n):
    for i in range(2, int(n / 2) + 1):
        if n % i == 0 and isprime(i):
            return i
