import no_req_mathematic as math

conditions = [math.isprime(5) is True,  # 1
              math.isprime(6) is False,  # 2
              math.arithmetic.divisers(66) == [1, 2, 3, 6, 11, 22, 33, 66],  # 3
              math.arithmetic.irreductible(4, 2) == 2,  # 4
              math.arithmetic.irreductible(18, 81) == (2, 9),  # 5
              math.arithmetic.prime_decomposition(2022) == [2, 3, 337],  # 6
              math.arithmetic.smallest_divider(121) == 11,  # 7
              math.functions.pgcd(247, 260) == 13,  # 8
              math.functions.ppcm(83, 37) == 3071,  # 9
              math.numbers.x_polis(2022, 3) == (True, [(163, 12), (504, 4), (673, 3)]),  # 10
              math.numbers.x_polis(2022, 4) == (False, -1),  # 11
              math.numbers.aba(5, 5) == [(8, 2, 2), (18, 2, 3), (24, 3, 2), (32, 2, 4), (50, 2, 5),  # 12
                                         (64, 4, 2), (81, 3, 3), (160, 5, 2), (192, 3, 4), (324, 4, 3),
                                         (375, 3, 5), (1024, 4, 4), (1215, 5, 3), (2500, 4, 5),
                                         (5120, 5, 4), (15625, 5, 5)]]

if all(conditions):
    print("All the tests succeeded!")
else:
    for i in range(0, len(conditions)):
        if not conditions[i]:
            print("Test", i + 1, "failed!")
print("Done!")
