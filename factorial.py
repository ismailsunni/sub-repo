def factorize(x):
    """Factorize a number.
    """
    if x == 0:
        return 1
    else:
        return x * factorize(x - 1)

