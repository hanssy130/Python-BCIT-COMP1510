def compound_interest(principal, rate, times_compounded, years):
    """
    Calculates the total after compound interest. Invest early!

    :param principal: float
    :param rate: float
    :param timescompounded: int
    :param years: float
    :precondition: Enter a principal amount and rate in dollars. Enter a time before the first interest collection.
    :postcondition: Calculates the total at the end of compound interest.
    :return: The grand total of the principal

    >>> compound_interest(100, 0.05, 2, 0.4) #If the amount of time left doesn't meet the first compounding.
    100.0
    >>> compound_interest(101, 0.08, 4, 10) #Regular example.
    223.01
    """
    if 1 / times_compounded > years:
        print(float(principal))
    else:
        total = float(principal*((1 + rate / times_compounded) ** (times_compounded * years)))
        print(float(round(total, 2)))




def main():
    """
    Drives the main function.
    """
    compound_interest(101, 0.08, 4, 10)


if __name__=="__main__":
    main()


"""
decomposition: The formula is straightforward. There was no decomposition needed to make this function.
patternmatching: There are no patterns, the formula was given to me.
abstraction: There is no abstraction.
algorithms: The algorithm was given to me by Chris the instructor.
"""