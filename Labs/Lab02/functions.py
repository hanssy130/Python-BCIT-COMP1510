def format_name(firstname, lastname):
    """
    Strip off blank space and capitalizes the first letter of each name.

    :param firstname: First Name
    :param lastname: Last Name
    :precondition: firstname must be a string
    :precondition: lastname must be a string
    :postcondition: removes white space and capitalizes the first letter and decapitalizes the other letters.
    :return: parameters with only one space in between and only the first letter is capitalized.
    """
    stripfname = firstname.lstrip()
    stripfname = stripfname.rstrip()
    striplname = lastname.lstrip()
    striplname = striplname.rstrip()
    capstripfname = stripfname.capitalize()
    capstriplname = striplname.capitalize()
    print(capstripfname + " " + capstriplname)


def tripler(parameter):
    """
    Triples a string.

    :param parameter: A string or integer.
    :return: a tripled parameter
    """
    strparameter = str(parameter)
    trips = strparameter + strparameter + strparameter
    print(trips)


def this_year():
    """
    Calculate the year 2019.
    """
    year = (10000 / 5) + 10 * 10 - 9 * 9
    print(year)


def base_conversion(num, base):
    """
    Converts a decimal number to the targeted base.

    :param num: an int
    :param base: an int
    :precondition: num must be an int
    :precondition: base must be an int
    :postcondition: conversion of num into the targeted base
    :return: number converted into targeted base
    """
    maxvalue = (base * base * base * base) - 1
    strmaxvalue = str(maxvalue)
    print(
        "The max value for the given base is " + strmaxvalue + ". Please enter a value that is equal or less than the max")

    quotient = int(num / base)
    d = str(num % base)
    qquotient = int(quotient / base)
    c = str(quotient % base)
    qqquotient = int(qquotient / base)
    b = str(qquotient % base)
    qqqquotient = int(qqquotient / base)
    a = str(qqquotient % base)

    result = int(a + b + c + d)
    print(result)

def main():
    """
    Drive the program.
​
    Tests the functions in this module.
    """
    format_name("   HAns    ", "    sY    ")
    format_name("   cheese    ", "    cake    ")
    tripler(56)
    tripler("yes")
    tripler("")
    tripler("101.0")
    base_conversion(55, 8)
    this_year()

if __name__ == "__main__":
    main()

