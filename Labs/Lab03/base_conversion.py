def base_conversion(num, base):
    """
    Prints what the maximum value of the given base is.

    :param num: an int
    :param base: an int
    :precondition: num must be an int
    :precondition: base must be an int
    :postcondition: string is created
    :return: Prints the max value.
    """

    maxvalue = (base * base * base * base) - 1
    strmaxvalue = str(maxvalue)
    print("The max value for the given base is " + strmaxvalue + ". Please enter a value that is equal or less than "
                                                                 "the max.")
    convertor(num, base)


def convertor(num, base):
    """
    Calculate the decimal into the base.

    :param num: int
    :param base: int
    :precondition: number and base must be an integer
    :postcondition: get a new integer
    :return: Calculated number in new base.
    """

    quotient = int(num / base)
    d = str(num % base)
    qquotient = int(quotient / base)
    c = str(quotient % base)
    qqquotient = int(qquotient / base)
    b = str(qquotient % base)
    qqqquotient = int(qqquotient / base)
    a = str(qqquotient % base)
    printer(a, b, c, d)


def printer(a, b, c, d):
    """
    Print the converted number.

    :param a: string
    :param b: string
    :param c: string
    :param d: string
    :return: Printed result.
    """
    result = int(a + b + c + d)
    print("The converted result is " + str(result) + ".")


def main():
    base_conversion(123, 8)
    print()


if __name__ == "__main__":
    main()
