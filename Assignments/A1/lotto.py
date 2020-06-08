import random


def number_generator():
    """
    Generates 6 lottery numbers

    :return: Sorted list (lowest to highest) of numbers between 1 to 49.
    """
    a = random.randint(1, 49)
    b = random.randint(1, 49)
    c = random.randint(1, 49)
    d = random.randint(1, 49)
    e = random.randint(1, 49)
    f = random.randint(1, 49)
    lotto = [a, b, c, d, e, f]
    return sorted(lotto)


def main():
    """
    Drives the main function.
    """
    print(number_generator())


if __name__=="__main__":
    main()

"""
decomposition: The program generates 6 random numbers, then lists them, then prints it. 
The program isn't complex enough for further decomposition.
pattern matching: Each number needs to be created the same way, so we repeat the random function 6 times.
abstract: We worry about ordering the numbers after they're generated than before.
algorithms: Each number needs to be created the same way and put into the list.
"""