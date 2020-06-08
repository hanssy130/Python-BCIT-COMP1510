import doctest

def gcd(a, b):
    """
    Determines the GCD of two numbers via Euclid's method.

    :param a: an int
    :param b: an int
    :precondition: Both parameters must be integers
    :postcondition: Calculates the Greatest Common Denominator
    :return: the denominator
    >>> gcd(270, 192)
    6
    >>> gcd(6, 0)
    'You cannot divide by zero!'
    """
    flag = False
    try:
        while not flag:
            remainder = a % b
            a = b
            b = remainder
            if remainder == 0:
                break
        return a
    except ZeroDivisionError:
        return "You cannot divide by zero!"


def main():
    the_gcd = gcd(10, 8)
    print(the_gcd)
    doctest.testmod()


if __name__=="__main__":
    main()