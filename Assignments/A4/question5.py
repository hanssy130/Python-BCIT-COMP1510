import doctest


def cash_money(amount):
    """
    Calculates the fewest amount of Canadian currency units to equate the amount.

    :param amount: a float
    :precondition: Float must have two decimal digits and be positive
    :postcondition: Promises to display the results
    :return: a dict
    >>> cash_money(22.22)
    {20: 1, 2: 1, 0.1: 2, 0.01: 2}
    >>> cash_money(989.94)
    {100: 9, 50: 1, 20: 1, 10: 1, 5: 1, 2: 2, 0.25: 3, 0.1: 1, 0.05: 1, 0.01: 4}
    """
    amount_remaining = amount
    breakdown = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]
    result = {}
    for value in breakdown:
        howMany = int(amount_remaining / value)
        amount_remaining = amount_remaining - howMany * value
        if howMany == 0:
            continue
        result[value] = howMany

    if 0.005 < amount_remaining < 0.01:
        result[0.01] = result[0.01] + 1
    return result


def main():
    breakdown = cash_money(984.94)
    print(breakdown)
    doctest.testmod()


if __name__ == "__main__":
    main()
