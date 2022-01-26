def x_polis(n, x):
    """
    Checks if a number n is a x-polis.

    Description:
    A x-polis is a number that can be written as the sum of consecutive numbers in x different ways.

    Parameters:
    n (int): The number to check
    x (int): The number of times the number n should be the sum of consecutive numbers

    Returns:
    tuple (boolean, dict(tuple(int)))
        boolean: If n is a x-polis or not.
        dict: The values where n is the sum of x consecutive numbers
            (x times)
            tuple: The values
                int: The first consecutive number
                int: The number of consecutive numbers such that n is the sum that number of numbers

    Exemples:
    input: x_polis(2022, 3)
    return: (True, [(163, 12), (504, 4), (673, 3)])

    """
    hits = []
    for i in range(1, round(n/2)+1):
        sums = 0
        j = 0
        while sums < n:
            sums += i+j
            j += 1
        if sums == n and j != 1:
            ret = (i, j)
            hits.append(ret)
            if len(hits) > x:
                return False, -1
    if len(hits) != x:
        return False, -1
    else:
        return True, hits
