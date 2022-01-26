def aba(max_a, max_b, min_a=2, min_b=2):
    res = []
    for a in range(min_a, max_a+1):
        for b in range(min_b, max_b+1):
            res.append((a * (b ** a), a, b))
    return sorted(res)
