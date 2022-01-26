from no_req_mathematic.arithmetic.prime_decomposition import *


def pgcd(x, y):
    dec_x = prime_decomposition(x)
    dec_y = prime_decomposition(y)
    dic_common = []
    common = 1
    for i in dec_x:
        if i in dec_y:
            dic_common.append(i)
            del dec_y[dec_y.index(i)]
    for j in dic_common:
        common *= j
    return common
