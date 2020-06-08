import doctest

def eratosthenes(upperbound):
    """
    Returns a list of primes between 0 and the upperbound.

    :param upperbound: a list
    :precondition: upperbound must be a list of numbers.
    :postcondition: calculates the primes betwen 0 and the upperbound.
    :return: a list of desired primes

    >>> eratosthenes(10)
    [2, 3, 5, 7]
    >>> eratosthenes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    if upperbound <= 0:
        raise ValueError(f"The value must be positive!")
    numlist = []
    for i in range(2, upperbound+1):
        numlist.append(i)
    for i in numlist:
        for j in range(i*i, upperbound+1, i):
            if j in numlist:
                numlist.remove(j)
    return numlist


def main():
    primes_below_30 = eratosthenes(10)
    print(primes_below_30)
    doctest.testmod()


if __name__ == "__main__":
    main()
