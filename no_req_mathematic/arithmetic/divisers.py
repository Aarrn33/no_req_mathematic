def divisers(x):
    """
    Gets all of the divisers of x

    Parameters:
        x: The number for which we need the divisers

    Returns:
        dict: All of the divisers of x
            (one time per divider)
            int: A divisers
    """
    res = []
    for i in range(1, int(x/2)+1):
        if x % i == 0:
            res.append(i)
    if x != 1:
        res.append(x)
    return res
