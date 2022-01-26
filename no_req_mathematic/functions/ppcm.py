from no_req_mathematic.arithmetic.prime_decomposition import *


def ppcm(x, y):
    dec_x = prime_decomposition(x)
    dec_y = prime_decomposition(y)
    dic_common = dec_x
    common = 1
    for i in dec_x:
        if i in dec_y:
            del dec_y[dec_y.index(i)]
    for n in dec_y:
        dic_common.append(n)
    for j in dic_common:
        common *= j
    return common
